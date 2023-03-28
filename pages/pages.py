import random
import urllib.parse
from web import response, redirect, HTTPRequest

def generate_data():
    info = []
    users = [
        {'First_name': 'John', 'Last_name': 'Doe', 'User_type': 'Student','User_id':random.randint(10000000, 99999999)},
        {'First_name': 'Jane', 'Last_name': 'Doe', 'User_type': 'Teacher', 'User_id': random.randint(10000000, 99999999)},
        {'First_name': 'Bob', 'Last_name': 'Smith', 'User_type': 'Staff','User_id': random.randint(10000000, 99999999)},
    ]
    products = [
        {'Product_type': 'Book', 'Product_name': 'The Great Gatsby', 'Product_id': random.randint(10000000, 99999999)},
        {'Product_type': 'Magazine', 'Product_name': 'National Geographic', 'Product_id': random.randint(10000000, 99999999)},
        {'Product_type': 'E-Book', 'Product_name': 'To Kill a Mockingbird', 'Product_id': random.randint(10000000, 99999999)},
        {'Product_type': 'Audio Book', 'Product_name': 'Harry Potter and the Sorcerer\'s Stone', 'Product_id': random.randint(10000000, 99999999)},
        {'Product_type': 'DVD', 'Product_name': 'The Lord of the Rings: The Fellowship of the Ring', 'Product_id': random.randint(10000000, 99999999)},
    ]
    SKU = random.randint(1000000000, 9999999999)
    TotalChecked = random.randint(0,1000)
    fine_status = ['Paid', 'Unpaid', 'Lost']
    Status = ['Checked Out','Held','Stock']
    for i in range(10):
        user = random.choice(users)
        product = random.choice(products)
        fine = round(random.uniform(0.01, 50.00),2)
        multiplier = round(random.uniform(1.00, 2.00),2)
        cost = round(random.uniform(1.00, 50.00),2)
        info.append({
            'User_type': user['User_type'],
            'First_name': user['First_name'],
            'Last_name': user['Last_name'],
            'User_Name': user['Last_name'] + ', ' + user['First_name'],
            'User_id': user['User_id'],
            'Product_type': product['Product_type'],
            'Product_name': product['Product_name'],
            'Product_id': product['Product_id'],
            'Cost': cost,
            'Fine_status': random.choice(fine_status),
            'Fine': fine,
            'Multiplier': multiplier,
            'SKU' :  SKU,
            'Total_Checked': TotalChecked,
            'Status': random.choice(Status)
        })
    return info




def ProductsCheckedOut(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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
   <h2>Reports &amp; Views</h2>
         <h1 style="background-color: #333; color: white; padding: 10px;">Products Checked Out</h1>
         <table  style="width:100%">
        <thead>
          <tr>
            <th>Product Type</th>
            <th>Product Name</th>
            <th>Product ID</th>
           </tr>
        </thead>
        <tbody>
    """
    for item in info:
        body += "<tr>"
        body += f"<td>{str(item['Product_type'])}</td>"
        body += f"<td>{str(item['Product_name'])}</td>"
        body += f"<td>{str(item['Product_id'])}</td>"
        body += "</tr>"

    body += """</tbody></table></body></html>"""
    return response(request, body, 200)

def ProductsFined(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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

    body += """</tbody></table></body></html>"""
    return response(request, body, 200)



def ProductMissing(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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

    body += """</tbody></table></body></html>"""
    return response(request, body, 200)




def ProductsInventory(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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

    body += """</tbody></table></body></html>"""
    return response(request, body, 200)

def ProductsInfo(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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

    body += """</tbody></table></body></html>"""
    return response(request, body, 200)
def UsersCheckedOut(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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

    body += """</tbody></table></body></html>"""
    return response(request, body, 200)
    
def CheckedOutBy(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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

    body += """</tbody></table></body></html>"""
    return response(request, body, 200)

def MissingProduct(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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

    body += """</tbody></table></body></html>"""
    return response(request, body, 200)

def UsersDisabled(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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
    body += """</tbody></table></body></html>"""
    return response(request, body, 200)

def UsersLifetimeTotalChecked(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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
    body += """</tbody></table></body></html>"""
    return response(request, body, 200)

def ItemStatus(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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
    body += """</tbody></table></body></html>"""
    return response(request, body, 200)

def UsersApplicable(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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
    body += """</tbody></table></body></html>"""
    return response(request, body, 200)
def ItemInfo(request: HTTPRequest):
    info = generate_data()
    body = f""" 
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
    body += """</tbody></table></body></html>"""
    return response(request, body, 200)