#coding=utf-8
import os
PORT=os.environ.get('PORT', '5000')

def http_server():
    import http.server
    import socketserver
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", int(PORT)), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


os.system('./ttyd.x86_64 -p ' + PORT + ' bash')        
