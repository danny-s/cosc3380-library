from web import response, redirect, HTTPRequest

def NavPage(request: HTTPRequest):
    nav = '''
<!DOCTYPE html>
<html>
<head>
    <title>Library Management System</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
        }
        header {
            background-color: #333;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 40px;
        }
        nav {
            background-color: #f2f2f2;
            overflow: hidden;
        }
        nav a {
            float: left;
            display: block;
            color: #333;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }
        nav a:hover {
            background-color: #ddd;
            color: black;
        }
    </style>
</head>
<body>
    <header>Library Management System</header>
    <nav>
        <a href="/ProductsFined">Products Fined</a>
        <a href="/ProductsMissing">Products Missing</a>
        <a href="/ProductsInInventory">Products In Inventory</a>
        <a href="/ProductsInfo">Products Information</a>
        <a href="/UsersCheckedOut">Users Checked Out</a>
        <a href="/CheckedOutBy">Checked Out By</a>
        <a href="/MissingProduct">Missing Product</a>
        <a href="/UsersDisabled">Users Disabled</a>
        <a href="/UsersLifetimeTotalChecked">Users Lifetime Total Checked</a>
        <a href="/ItemStatus">Item Status</a>
        <a href="/UsersApplicable">Users Applicable</a>
        <a href="/ItemInfo">Item Info</a>
    </nav>
</body>
</html>
'''
    return response(request, nav, 200)