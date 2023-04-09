import urllib.parse

from web import response, redirect, HTTPRequest


def example_get_response(request: HTTPRequest):
    
    body = """
    <html>
    <head><style>
        html, body {
            padding: 25px;
            display: block;
        }
    </style></head>
    <body>
        <h2>
            Library Login
        </h2>
        <div>
            Enter your username and password.
        </div>
        <form method="post" action="/example/submit" enctype='multipart/form-data'>
            <label for="un">Username</label><br>
            <input type="text" name=un id=un><br>
            <label for="pw">Password</label><br>
            <input type="text" name=pw id=pw><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """

    return response(request, body, 200)


def example_post_response(request: HTTPRequest):
    # breakpoint()
    success = 0
 #   if un := request.data["un"]:
  #      text = un[0]
   ##        success = 1
    #if pw:= request.data["pw"]:
    #   text = pw[0]
            #success = 1

    text = urllib.parse.urlencode({"un": success, "text": text})
    text = urllib.parse.urlencode({"pw": success, "text": text})

    return redirect(request, f"/Welcome?{text}")


#def hello(request: HTTPRequest):
 #   if "1" in request.query.get("un", []):
   #     body = "This is your username: {un}"
   # else:
    #    body = "Username unavailable. Try again"
    #    if text := request.query.get("text", ["nothing"])[0]:
     #       body += f" you said '{text}'"
    #return response(request, body)
    
    
    
 #############################################################

<!DOCTYPE html>
<html>
    <head><style>
        html, body {
            padding: 25px;
            display: block;
        }
    </style></head>
    <body>
        <h2>
            Create an Account
        </h2>
        <div>
            Enter your first and last name.
        </div>
        <form method="post" action="/action_page.php" enctype='multipart/form-data'>
            <label for="fname">First Name</label><br>
            <input type="text" name=fname id=fname><br>
            <label for="lname">Last Name</label><br>
            <input type="text" name=lname id=lname>
            <div>
            Enter your username.    
            </div>
            <label for="un">Username</label><br>
            <input type="text" name=un id=un><br>
            <div>
            Enter your password.
            </div>
			<label for="pw">Password</label><br>
            <input type="text" name=pw id=pw><br>
            <input type="submit" value="Submit">
        </form>    
    </body>
</html>

#################################################################
