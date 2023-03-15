from pathlib import Path
from typing import BinaryIO, Iterable, Union

import io_
from io_ import PathLike
from typing_ import Headers, Status, ResponseBody, QuerySet

DEFAULT_BLOCK_SIZE = 256000

class MultiField:
    def __init__(self, fields: Headers=None):        
        if isinstance(fields, MultiField): # construct from another headers
            self._fields = fields.as_list()
        elif isinstance(fields, dict):
            self._fields = list(fields.items())
        else:
            self._fields = list(fields or [])
    
    def set_field(self, key, value):
        # clear all field with given key and set value
        self.clear_field(key)
        self.add_field(key, value)
        
    def add_field(self, key, value):
        # add field without removing
        self._fields.append((key.lower(), value))
    
    def clear_field(self, key):
        key = key.lower()
        pos = [i for i in range(len(self._fields)-1, -1, -1) if self._fields[i] == key]
        for i in pos:
            self._fields.remove(i)
    
    def keys(self) -> list[str]:
        return tuple({k for k, _ in self._fields})
    
    def __iter__(self):
        return self._fields.__iter__()

    def as_list(self) -> list[tuple[str, str]]:
        return list(self._fields)
    
    def as_qs(self) -> QuerySet:
        return {k: [v for i, v in self._fields if k == i] for k in self.keys()}

    def qs_update(self, qs: QuerySet):
        for k, vs in qs.items():
            for v in vs:
                self.add_field(k, v)



class HTTPRequest:
    def __init__(self, env, query=None, data=None, body: bytes=None):
        self.env: dict = env
        self.query: dict[str, list[str]] = query
        self.data: dict[str, list[str]] = data
        self.body: bytes = body or b''

    @property
    def text(self):
        return str(self.body, 'utf-8')


class HTTPResponse:
    def __init__(self, status: Status, body: ResponseBody=None, headers: Headers=None, data=False) -> None:
        self.status = str(status) + ' ' if isinstance(status, int) else status
        self.headers = MultiField(headers)

        # automatically adds content type html to headers if data=False
        if not data and 'content-type' not in self.headers.keys():
            self.headers.add_field('content-type', 'text/html; charset=utf-8')

        # wsgi requires an iterable body that can be sent across multiple messages.
        # if you get an iteration error, you're not passing an appropriate iterable
        # to the body parameter. 
        self.body: Iterable
        if isinstance(body, str) or body is None:
            self.body = [bytes(body or "", 'utf-8')]
        elif isinstance(body, bytes):
            self.body = [body]  # custom body bytes specified.
        else:
            self.body = iter(body) # must be an iterable of bytes


def response(request: HTTPRequest, body: ResponseBody=None, status: Status=None, headers: Headers = None) -> HTTPResponse:
    return HTTPResponse(status or "200 OK", body, headers)


def redirect(request: HTTPRequest, to: str, status: Status="302 Found", headers: Headers = None) -> HTTPResponse:
    # Don't use this, it's bugged.
    headers = MultiField()
    headers.set_field('Location', to)
    return response(request, None, status, headers)

def error_response(request: HTTPRequest, status: Status="403 Forbidden", body: ResponseBody=None, headers: Headers=None) -> HTTPResponse:
    if body is None:
        body = f"The server reported this action as an error ({status})."
    return response(body, status, headers)

def file_response(request: HTTPRequest, path: PathLike, status: Status=None, headers: Headers=None, block_size=DEFAULT_BLOCK_SIZE) -> HTTPResponse:
    # send stream 
    path = io_.to_path(path)
    headers = Headers(headers or MultiField())
    headers.set['Content-Disposition'] = f'attachment; filename="{path.name}"'
    
    file = open(path, 'rb')
    return data_response(request, file, status, headers, block_size)
   

def data_response(request: HTTPRequest, stream: BinaryIO, status: Status=None, headers: Headers = None, block_size=DEFAULT_BLOCK_SIZE) -> HTTPResponse:
    if 'wsgi.file_wrapper' in request.env:
        data = request.env['wsgi.file_wrapper'](stream, block_size)
    else:
        # wsgi file wrapper iterator already implements close, so we only
        # need to safe_iter this one
        data = io_.safe_iter(iter(lambda: stream.read(block_size), b''), stream.close())

    return response(io_.safe_iter(data, data.close),status,headers,data=True)

class HTTPServerFailure(Exception):
    def __init__(self, code: int=500, message: str=None, *a, **kw):
        self.code = code
        self.message = message if message is not None else f"{code} Internal Server Error"
        super().__init__(code, message, *a, **kw)

def static_files(to: Union[Path, str],  template: str=None):
    # generates proxy response handler function that serves
    # the files in path `to`. `template` strips out the first part of
    # the requesting url

    # ensure this is a Path object so the path works on
    # any operating system
    to = io_.to_path(to)
     
    def templated_static_response(request: HTTPRequest):
        url_path = request.env.get('REQUEST_METHOD', '')

        if '..' in url_path:
            return error_response(request, "403 Forbidden", "Parent paths (..) not allowed for static urls.")

        if template and url_path.startswith(template): # strip template from url
            url_path = url_path[template.length()-1:]

        file_path = to / url_path.strip('/')
        if not file_path.is_file():
            return error_response(request, "404 Not Found", "Requested file was not found on this server.")

        return file_response(request, file_path, "200 OK")
        
    return templated_static_response
