from typing import Callable
from urllib import parse
import re
import multipart

from web import (
    HTTPResponse,
    HTTPServerFailure,
    response,
    HTTPRequest,
    DEFAULT_BLOCK_SIZE,
    MultiField,
)
from typing_ import QuerySet


class Application:
    def __init__(self):
        self.urls = {}

    def register(self, url: str, handler: callable, request_type=None):
        """
        Registration function for associating urls with handlers.

        If request_type is not set or None, the url becomes the default for any request type
        without a designated handler
        """
        if request_type is not None:
            request_type = request_type.upper()
        self.urls.setdefault(url, {})[request_type] = handler

    def resolve(self, environ: dict) -> Callable[[HTTPRequest], HTTPResponse]:
        # "standard environ keys" https://wsgi.readthedocs.io/en/latest/definitions.html
        try:
            url: dict = self.urls[environ["PATH_INFO"]]
        except KeyError:
            url: dict = None
            for pattern in self.urls:
                if re.match(pattern, environ["PATH_INFO"]):
                    url = self.urls[pattern]
            if url is None:
                raise HTTPServerFailure(
                    404,
                    f"URL {environ['PATH_INFO']} DOES NOT APPEAR TO MATCH ANY REGISTERED URLS!",
                )

        try:
            handler = url.get(environ["REQUEST_METHOD"], None) or url[None]
        except KeyError:
            raise HTTPServerFailure(
                404,
                f"URL {environ['REQUEST_METHOD']} DOES NOT APPEAR TO HAVE A "
                f"DEFAULT HANDLER OR HANDLER FOR REQUESTS OF TYPE {environ['REQUEST_METHOD']}.\n"
                f"available handlers: {url.keys()}",
            )

        return handler


def process_env_data(environ: dict) -> HTTPRequest:
    body = b""

    query: QuerySet = {}
    if qs := environ.get("QUERY_STRING", ""):
        query = parse.parse_qs(qs, True)

    data = MultiField()
    if "application/x-www-form-urlencoded" in environ.get("CONTENT_TYPE", ""):
        data.qs_update(query)
    if "multipart/form-data" in environ.get("CONTENT_TYPE", ""):
        form = multipart.parse_form_data(environ, strict=True)[0]
        data.qs_update({k: form.getall(k) for k in form.keys()})
    else:  # not form, parse normally
        pass
        # while block := environ['wsgi.input'].read(DEFAULT_BLOCK_SIZE) != b'':
        #     body += block
    # breakpoint()
    return HTTPRequest(environ, query, data.as_qs(), body)


# global application instance
App = Application()


def register(*a, **kw):
    App.register(*a, **kw)


def wsgi_application(environ, start_response):
    req_type = environ["REQUEST_METHOD"]
    req_url = environ["PATH_INFO"] + environ.get("QUERY_STRING", "")
    req_client = environ.get("REMOTE_ADDR", "")

    try:
        handler = App.resolve(environ)
        resp = handler(process_env_data(environ))
    except HTTPServerFailure as e:
        status = e.code
        err = e.message
        resp = response(None, f"server error ({status})! Info:\n{err}", status)
        print(f"SERVER ERROR: {err}")

    status = resp.status
    headers = resp.headers.as_list()

    print(f"Received {req_type} from {req_client}: {req_url} ({status})")

    start_response(status, headers)
    return resp.body
