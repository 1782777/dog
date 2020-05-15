
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result': 'this is a http server test'}
host = ('172.0.0.1', 8080)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        
    def do_POST(self):
        data = self.rfile.read(int(self.headers["content-length"]))
        for field in form.keys():
            print(field)

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting http server, listen at: %s:%s" % host)
    server.serve_forever()
