
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result': 'this is a http server test'}
host = ('182.92.114.73', 8080)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        
    def go_POST(self):
        data = self.rfile.read(int(self.headers["content-length"]))
        print(data)

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting http server, listen at: %s:%s" % host)
    server.serve_forever()
