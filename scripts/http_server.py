import os
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Check for command-line arguments
if len(sys.argv) < 2:
    print("Usage: python http_server.py file1 [file2 ... fileN]")
    sys.exit(1)

# Build the file map from command-line arguments
FILE_MAP = {os.path.basename(file): os.path.abspath(file) for file in sys.argv[1:] if os.path.isfile(file)}

if not FILE_MAP:
    print("No valid files found. Please provide valid file paths.")
    sys.exit(1)

class CustomHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Remove leading slash and map to the actual file path
        virtual_file = path.lstrip("/")
        if virtual_file in FILE_MAP:
            return FILE_MAP[virtual_file]
        # File not found
        return None

    def do_GET(self):
        # Override to handle 404 for unmapped files
        if self.translate_path(self.path):
            super().do_GET()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

# Start the server
PORT = 8000
server = HTTPServer(("localhost", PORT), CustomHandler)
print(f"Serving on http://localhost:{PORT}")
print("Serving files:")
for virtual, real in FILE_MAP.items():
    print(f"  {virtual} -> {real}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server.")