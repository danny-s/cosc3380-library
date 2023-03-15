from app import register
from web import static_files
from pages import example

register("/example/page", example.example_get_response, "get")
register("/example/submit", example.example_post_response, "post")
register("/hello", example.hello)
# register(r"\/static\/.*", static_files("static/", "/static/"))
# register("/favicon.ico", static_files("static/favicon.ico"))
