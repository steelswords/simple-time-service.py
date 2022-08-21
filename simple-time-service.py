#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

host = "0.0.0.0"
port = 8086

class SimpleTimeServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        now = time.gmtime()
        self.wfile.write(bytes(f"{now.tm_year}\n{now.tm_mon}\n{now.tm_hour}\n{now.tm_min}\n{now.tm_sec}\n", "utf-8"))

if __name__ == "__main__":
    server = HTTPServer((host, port), SimpleTimeServer)
    print(f"Server started. Listening at {host}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Stopped server.")


