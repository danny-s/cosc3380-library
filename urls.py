from app import register
from web import static_files
from pages import accounts

register("/example/page", accounts.example_get_response, "get")
register("/example/submit", accounts.example_post_response, "post")
register("/hello", accounts.hello)
# register(r"\/static\/.*", static_files("static/", "/static/"))
# register("/favicon.ico", static_files("static/favicon.ico"))
