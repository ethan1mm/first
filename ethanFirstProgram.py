# print("Ethan Says Hi!")  # a simple test line that is commented out so it doesn't run

# Save as hello.py  # suggestion for a filename if you want to save this example
# Ethan's first program  # a tiny program that starts a web server and shows messages
from http.server import HTTPServer, BaseHTTPRequestHandler  # import the server building blocks
import os  # import os to find files in the project folder


class SimpleHandler(BaseHTTPRequestHandler):  # make a new handler to answer web requests
    def do_GET(self):  # this function runs when someone visits the page in a browser
        # If the browser requests the local image path, serve the file bytes
        if self.path == "/elephant.png":
            img_path = os.path.join(os.path.dirname(__file__), "elephant.png")
            try:
                with open(img_path, "rb") as f:
                    data = f.read()
                self.send_response(200)
                self.send_header("Content-type", "image/png")
                self.send_header("Content-length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            except FileNotFoundError:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"elephant.png not found")
            return

        # Otherwise return the HTML page that references the local image
        self.send_response(200)  # send "200 OK" which means the page loaded fine
        self.send_header("Content-type", "text/html")  # tell the browser the content is HTML
        self.end_headers()  # finish the header section so we can send the page body
        for _ in range(2):  # do the next two lines two times so messages show twice
            self.wfile.write(b"<h1>Ethan Says Hi</h1>")  # write bytes for the first headline
            self.wfile.write(b"<h1>Dad Says Hi</h1>")  # write bytes for the second headline
        # include the local image by path so the browser requests /elephant.png
        self.wfile.write(b'<p><img src="/elephant.png" alt="elephant" width="1000"></p>')  # show the image
     
print("Open http://localhost:8000 in browser")  # tell whoever ran the script where to go
HTTPServer(("localhost", 8000), SimpleHandler).serve_forever()  # start the server and keep running