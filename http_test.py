
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi

data = {'result': 'this is a http server test'}
host = ('127.0.0.1', 8080)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        
    def do_POST(self):
        #data = self.rfile.read(int(self.headers["content-length"]))
        form =cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD':'POST',
                'CONTENT_TYPE':self.headers['Content-Type'],
            }
        )
        for field in form.keys():
            field_items = form[field]
            print(field_items.filename)
            print(field_items.value)

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting http server, listen at: %s:%s" % host)
    server.serve_forever()
