import json
from urllib.parse import parse_qs


# Load JSON once
with open("marks.json", "r") as f:
    marks_data = json.load(f)


def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"

    # Parse query params
    params = parse_qs(request.query_string.decode())
    names = params.get("name", [])

    # Look up marks, use None if name not found
    marks = []
    for i in range(len(marks_data)):
        if(marks_data[i].get("name") in names[0]):
            marks.append(marks_data[i].get("marks"))

    return response.json({"marks": marks})



from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return