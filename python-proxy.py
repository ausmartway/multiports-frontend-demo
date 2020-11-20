import os
import socketserver
import http.server
import urllib.request

SERVICE1_URL = os.environ.get('SERVICE1_URL')
SERVICE2_URL = os.environ.get('SERVICE2_URL')

PORT = 9088
class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url=self.path[1:]
        print("URL:",url)
        if url == "service1":
            self.send_response(200)
            self.end_headers()
            self.copyfile(urllib.request.urlopen(SERVICE1_URL), self.wfile)
        elif url == "service2":
            self.send_response(200)
            self.end_headers()
            self.copyfile(urllib.request.urlopen(SERVICE2_URL), self.wfile)
        else:
            self.send_response(404)
            self.end_headers()
        pass
    

httpd = socketserver.ForkingTCPServer(('', PORT), MyProxy)
print("Now serving at",str(PORT))
httpd.serve_forever()

