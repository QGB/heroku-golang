#coding=
import os
PORT=os.environ.get('PORT', '5000')


import http.server
import socketserver
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()