import urllib.parse
from web import response, redirect, HTTPRequest

def example_get_response(request: HTTPRequest):
    """
    request is an object containing request.env, a WSGI environ
    object containing request info:
    https://wsgi.readthedocs.io/en/latest/definitions.html
    - see "Standard environ keys" for most important info.
    """

    print("HIHIHIHIHIHIHIHIHI+++++++++++++++++++++++==")

    body = """
    <html>
    <head><style>
        html, body {
            padding: 25px;
            display: block;
        }
    </style></head>
    <body>
        <div>
            Here's an example of a basic html page.
        </div>
        <div>
            You'll save yourself a lot of effort if you use
            a templating library such as Jinja so you don't
            need to use inline html strings like I am. Up
            to you.
        </div>
        <div>
            Please say "hi" and press submit:
        </div>
        <form method="post" action="/example/submit" enctype='multipart/form-data'>
            <input type="text" name="hi_data" id="hi_data">
            <input type="submit" value="Send!">
        </form>
    </body>
    </html>
    """

    return response(request, body, 200)


def example_post_response(request: HTTPRequest):
    """
    Requests will have a query attribute (for url ?query= type data)
    and data attribute (for form-type data). Requests will also
    have an `env` attribute containing
    """

    # breakpoint()
    success = 0
    if hi_data := request.data["hi_data"]:
        text = hi_data[0]
        if "hi" in hi_data:
            success = 1

    text = urllib.parse.urlencode({"hi": success, "text": text})
    return redirect(request, f"/hello?{text}")


def hello(request: HTTPRequest):
    if "1" in request.query.get("hi", []):
        body = "Congrats!!!!! hi!!!!!!!!"
    else:
        body = "You didn't say 'hi' right :("
        if text := request.query.get("text", ["nothing"])[0]:
            body += f" you said '{text}'"
    return response(request, body)


