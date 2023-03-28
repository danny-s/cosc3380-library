from app import register
from web import static_files
from pages import pages
from pages import example
from pages import QueriesReportNav
register("/example/page", example.example_get_response, "get")
register("/example/submit", example.example_post_response, "post")
register("/hello", example.hello)


register("/ProductsCheckedOut",pages.ProductsCheckedOut,"get") #establishes the web
register("/ProductsFined",pages.ProductsFined,"get")
register("/ProductsMissing",pages.ProductMissing,"get")
register("/ProductsInInventory",pages.ProductsInventory,"get")
register("/ProductsInfo",pages.ProductsInfo,"get")
register("/UsersCheckedOut",pages.UsersCheckedOut,"get")
register("/CheckedOutBy",pages.CheckedOutBy,"get")
register("/MissingProduct",pages.MissingProduct,"get")
register("/UsersDisabled",pages.UsersDisabled,"get")
register("/UsersLifetimeTotalChecked",pages.UsersLifetimeTotalChecked,"get")
register("/ItemStatus",pages.ItemStatus,"get")
register("/UsersApplicable",pages.UsersApplicable,"get")
register("/ItemInfo",pages.ItemInfo,"get")
register("/QueriesReportHome",QueriesReportNav.NavPage,"get")


# register(r"\/static\/.*", static_files("static/", "/static/"))
# register("/favicon.ico", static_files("static/favicon.ico"))
