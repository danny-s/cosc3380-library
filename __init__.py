from wsgiref.simple_server import make_server
from app import wsgi_application
import urls  ## important to register all urls


if __name__ == "__main__":
    port = 8052
    host = "localhost"
    httpd = make_server(host, port, wsgi_application)
    print(f"Basic server listening on {host}:{port}")
    httpd.serve_forever()
