#print("Ethan Says Hi!")

# Save as hello.py
# Ethan's first program
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Ethan Says Hi</h1>")
        self.wfile.write(b"<h1>Dad Says Hi</h1>")

print("Open http://localhost:8000 in browser")
HTTPServer(("localhost", 8000), SimpleHandler).serve_forever()