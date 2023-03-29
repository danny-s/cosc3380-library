from app import register

from pages import reports, example

register("/example/page", example.example_get_response, "get")
register("/example/submit", example.example_post_response, "post")
register("/hello", example.hello)

for viewname, func in reports.report_views.items():
    # register generated views from reports
    register("/reports/" + viewname.title().replace("_", ""), func, "get")


# register(r"\/static\/.*", static_files("static/", "/static/"))
# register("/favicon.ico", static_files("static/favicon.ico"))
