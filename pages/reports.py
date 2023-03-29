import random

from web import response, HTTPRequest


def get_report(view: str):
    """
    returns data of corresponding view on database.
    """
    query = f"SELECT * FROM library.{view};"  # passed to connection object

    info = []
    users = [
        {
            "First_name": "John",
            "Last_name": "Doe",
            "User_type": "Student",
            "User_id": random.randint(10000000, 99999999),
        },
        {
            "First_name": "Jane",
            "Last_name": "Doe",
            "User_type": "Teacher",
            "User_id": random.randint(10000000, 99999999),
        },
        {
            "First_name": "Bob",
            "Last_name": "Smith",
            "User_type": "Staff",
            "User_id": random.randint(10000000, 99999999),
        },
    ]
    products = [
        {
            "Product_type": "Book",
            "Product_name": "The Great Gatsby",
            "Product_id": random.randint(10000000, 99999999),
        },
        {
            "Product_type": "Magazine",
            "Product_name": "National Geographic",
            "Product_id": random.randint(10000000, 99999999),
        },
        {
            "Product_type": "E-Book",
            "Product_name": "To Kill a Mockingbird",
            "Product_id": random.randint(10000000, 99999999),
        },
        {
            "Product_type": "Audio Book",
            "Product_name": "Harry Potter and the Sorcerer's Stone",
            "Product_id": random.randint(10000000, 99999999),
        },
        {
            "Product_type": "DVD",
            "Product_name": "The Lord of the Rings: The Fellowship of the Ring",
            "Product_id": random.randint(10000000, 99999999),
        },
    ]
    SKU = random.randint(1000000000, 9999999999)
    TotalChecked = random.randint(0, 1000)
    fine_status = ["Paid", "Unpaid", "Lost"]
    Status = ["Checked Out", "Held", "Stock"]
    for i in range(10):
        user = random.choice(users)
        product = random.choice(products)
        fine = round(random.uniform(0.01, 50.00), 2)
        multiplier = round(random.uniform(1.00, 2.00), 2)
        cost = round(random.uniform(1.00, 50.00), 2)
        info.append(
            {
                "User_type": user["User_type"],
                "First_name": user["First_name"],
                "Last_name": user["Last_name"],
                "User_Name": user["Last_name"] + ", " + user["First_name"],
                "User_id": user["User_id"],
                "Product_type": product["Product_type"],
                "Product_name": product["Product_name"],
                "Product_id": product["Product_id"],
                "Cost": cost,
                "Fine_status": random.choice(fine_status),
                "Fine": fine,
                "Multiplier": multiplier,
                "SKU": SKU,
                "Total_Checked": TotalChecked,
                "Status": random.choice(Status),
            }
        )
    return info


def report_template():
    header = f""" 
    <html>
    <style>
    body{{
        background-color: #f2f2f2;
        color: #333333;
        font-family: Arial, sans-serif;
    }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        background-color: #FFFFFF;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    }}
    th ,td {{
        text-align: left;
        padding: 12px;

    }}
    th {{
        background-color: #333333;
        color: #FFFFFF;
    }}
    tr:nth-child(even){{
    background-color: #f2f2f2;
    }}
    </style>
    <body>
    """

    footer = """</table></body></html>"""

    return header, footer


def generate_report(view: str, columns: dict[str, str], label: str = None):
    """
    Creates a page function reporting on a defined view.
    Using a 'function factory' pattern helps avoid boilerplate.

    view: name of view on database
    label: name given to html table on page
    columns: dict of colid, label pairs. colid is the name of the col in the view,
             label is the string visible for the column in the html table.
    """

    if label is None:
        label = view.replace("_", " ").title()

    # generate the body template when the server starts
    # this is called "preprocessing" and saves cpu cycles.
    # the only html being generated when a request is made is
    # derived from the data
    header, footer = report_template()

    # this can be preprocessed because it doesn't depend on data
    thead = "<thead><tr>"
    for col_label in columns.values():
        thead += f"<th>{col_label}</th>"
    thead += "</tr></thead>"

    def page_func(request: HTTPRequest):
        data = get_report(view)

        # iterate through data and generate table
        # this can't be preprocessed because it depends
        # on the data when the request is made
        tbody = "<tbody>"
        for line in data:
            tbody += "<tr>"
            for col in columns.keys():
                tbody += f"<td>{line[col]}</td>"
            tbody += "</tr>"
        tbody += "</tbody>"

        body = f"""
            <h2>Reports and Views</h2>
            <h1 style="background-color: #333; color: white; padding: 10px;">{label}</h1>
            <table  style="width:100%">
                {thead}
                {tbody}
            </table>
        """

        return response(request, header + body + footer, 200)

    return page_func


# These will be the actual descriptions of views we care about
# and their corresponding columns
# this current setup will generate /reports/ProductsCheckedOut and /reports/ProductsFined
report_listings = {
    "products_checked_out": ("Product_id", "Product_name", "Product_type"),
    "products_fined": (
        "Product_type",
        "Product_name",
        "Product_id",
        "Fine",
        "Multiplier",
        "Fine_status",
    ),
}

report_views = {}
for view, cols in report_listings.items():
    # create dict of column: pretty label pairs
    columns = {col: col.title().replace("_", " ") for col in cols}

    # generate a new response function for each view
    report_views[view] = generate_report(view, columns)


# KEVIN MESSAGE
# Deleted Products Checked Out, replaced with templated function as above. See urls.py for details.
# Remove this message and the following response functions, replacing them with their
# templated urls as shown.


def ProductsFined(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
   <h2>Reports &amp; Views</h2>
         <h1 style="background-color: #333; color: white; padding: 10px;">Products Fined</h1>
         <table  style="width:100%">
        <thead>
          <tr>
             <th>Product Type</th>
             <th>Product Name</th>
             <th>Product ID</th>
             <th>Fine</th>
             <th>Multiplier</th>
             <th>Fine Status</th>
           </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['Product_id'])}</td>"
        body += f"<td>{str(item['Fine'])}</td>"
        body += f"<td>{str(item['Multiplier'])}</td>"
        body += f"<td>{str(item['Fine_status'])}</td>"
        body += "</tr>"

        return response(request, header + body + footer, 200)


def ProductMissing(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
   <h2>Reports &amp; Views</h2>
         <h1 style="background-color: #333; color: white; padding: 10px;">Products Missing</h1>
         <table  style="width:100%">
        <thead>
          <tr>
             <th>Product Type</th>
             <th>Product Name</th>
             <th>Product ID</th>
             <th>Cost</th>
           </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['Product_id'])}</td>"
        body += f"<td>{str(item['Cost'])}</td>"
        body += "</tr>"

        return response(request, header + body + footer, 200)


def ProductsInventory(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
   <h2>Reports &amp; Views</h2>
         <h1 style="background-color: #333; color: white; padding: 10px;">Products In Inventory</h1>
         <table  style="width:100%">
        <thead>
          <tr>
             <th>Product Type</th>
             <th>Product Name</th>
             <th>Product ID</th>
             <th>Cost</th>
           </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['Product_id'])}</td>"
        body += f"<td>{str(item['Cost'])}</td>"
        body += "</tr>"

        return response(request, header + body + footer, 200)


def ProductsInfo(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
   <h2>Reports &amp; Views</h2>
         <h1 style="background-color: #333; color: white; padding: 10px;">Products Info</h1>
         <table  style="width:100%">
        <thead>
          <tr>
             <th>Product Type</th>
             <th>Product Name</th>
             <th>Product ID</th>
             <th>Cost</th>
           </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['Product_id'])}</td>"
        body += f"<td>{str(item['Cost'])}</td>"
        body += "</tr>"

        return response(request, header + body + footer, 200)


def UsersCheckedOut(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
   <h2>Reports &amp; Views</h2>
         <h1 style="background-color: #333; color: white; padding: 10px;">Users Checked Out</h1>
         <table  style="width:100%">
        <thead>
          <tr>
             <th>User Name</th>
             <th>User Type</th>
             <th>User ID</th>
             <th>Product Type</th>
             <th>Product Name</th>
             <th>Product ID</th>
           </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['User_Name'])}</td>"
        body += f"<td>{str(item['User_type'])}</td>"
        body += f"<td>{str(item['User_id'])}</td>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['Product_id'])}</td>"
        body += "</tr>"

        return response(request, header + body + footer, 200)


def CheckedOutBy(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
   <h2>Reports &amp; Views</h2>
         <h1 style="background-color: #333; color: white; padding: 10px;">Products held by</h1>
         <table  style="width:100%">
        <thead>
          <tr>
             <th>User Name</th>
             <th>User Type</th>
             <th>User ID</th>
             <th>Product Type</th>
             <th>Product Name</th>
             <th>Product ID</th>
           </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['User_Name'])}</td>"
        body += f"<td>{str(item['User_type'])}</td>"
        body += f"<td>{str(item['User_id'])}</td>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['Product_id'])}</td>"
        body += "</tr>"

        return response(request, header + body + footer, 200)


def MissingProduct(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
   <h2>Reports &amp; Views</h2>
         <h1 style="background-color: #333; color: white; padding: 10px;">Missing Products</h1>
         <table  style="width:100%">
        <thead>
          <tr>
             <th>User Name</th>
             <th>User Type</th>
             <th>ID</th>
             <th>Product Type</th>
             <th>Product Name</th>
             <th>Product ID</th>
             <th>SKU</th>
             <th>Cost</th>
           </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['User_Name'])}</td>"
        body += f"<td>{str(item['User_type'])}</td>"
        body += f"<td>{str(item['User_id'])}</td>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['Product_id'])}</td>"
        body += f"<td>{str(item['SKU'])}</td>"
        body += f"<td>{str(item['Cost'])}</td>"
        body += "</tr>"

        return response(request, header + body + footer, 200)


def UsersDisabled(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
<h2>Reports &amp; Views</h2>
        <h1 style="background-color: #333; color: white; padding: 10px;">Users Disabled</h1>
        <table  style="width:100%">
        <thead>
        <tr>
            <th>User Name</th>
            <th>User Type</th>
            <th>User ID</th>
        </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['User_Name'])}</td>"
        body += f"<td>{str(item['User_type'])}</td>"
        body += f"<td>{str(item['User_id'])}</td>"
        body += "</tr>"
        return response(request, header + body + footer, 200)


def UsersLifetimeTotalChecked(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
<h2>Reports &amp; Views</h2>
        <h1 style="background-color: #333; color: white; padding: 10px;">Products In Inventory</h1>
        <table  style="width:100%">
        <thead>
        <tr>
            <th>User Name</th>
            <th>User Type</th>
            <th>User ID</th>
            <th>Total Checked</th>
        </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['User_Name'])}</td>"
        body += f"<td>{str(item['User_type'])}</td>"
        body += f"<td>{str(item['User_id'])}</td>"
        body += f"<td>{str(item['Total_Checked'])}</td>"
        body += "</tr>"
        return response(request, header + body + footer, 200)


def ItemStatus(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
<h2>Reports &amp; Views</h2>
        <h1 style="background-color: #333; color: white; padding: 10px;">Products In Inventory</h1>
        <table  style="width:100%">
        <thead>
        <tr>
            <th>Product Type</th>
            <th>Product Name</th>
            <th>Product ID</th>
            <th>SKU</th>
            <th>Status</th>
        </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['Product_id'])}</td>"
        body += f"<td>{str(item['SKU'])}</td>"
        body += f"<td>{str(item['Status'])}</td>"
        body += "</tr>"
        return response(request, header + body + footer, 200)


def UsersApplicable(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
<h2>Reports &amp; Views</h2>
        <h1 style="background-color: #333; color: white; padding: 10px;">Products In Inventory</h1>
        <table  style="width:100%">
        <thead>
        <tr>
            <th>User ID</th>
            <th>User Name</th>
            <th>Product Type</th>
            <th>Item Name</th>
            <th>SKU</th>
            <th>Cost</th>
        </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['User_id'])}</td>"
        body += f"<td>{str(item['User_Name'])}</td>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['SKU'])}</td>"
        body += f"<td>{str(item['Cost'])}</td>"
        body += "</tr>"
        return response(request, header + body + footer, 200)


def ItemInfo(request: HTTPRequest):
    info = generate_data()
    header, footer = report_template()
    body = f"""
<h2>Reports &amp; Views</h2>
        <h1 style="background-color: #333; color: white; padding: 10px;">Products In Inventory</h1>
        <table  style="width:100%">
        <thead>
        <tr>
            <th>Product Type</th>
            <th>Item Name</th>
            <th>SKU</th>
            <th>Cost</th>
        </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['SKU'])}</td>"
        body += f"<td>{str(item['Cost'])}</td>"
        body += "</tr>"
        return response(request, header + body + footer, 200)


def NavPage(request: HTTPRequest):
    nav = """
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
"""
    return response(request, nav, 200)
