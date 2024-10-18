import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    This class handles incoming HTTP requests for the Simple API.
    It inherits from BaseHTTPRequestHandler to implement the required methods.
    """

    def do_GET(self):
        """
        Handles GET requests.

        Depending on the requested path, it responds with different data:
        - For the root path (/), it sends a simple text message.
        - For the /data endpoint, it sends a JSON response with sample data.
        - For the /status endpoint, it returns the API status.
        - For any other endpoint, it returns a 404 Not Found error with a message.
        """
        if self.path == '/':
            self.send_response(200)  
            self.send_header('Content-Type', 'text/plain')  
            self.end_headers()  
            self.wfile.write(b'Hello, this is a simple API!')  

        elif self.path == '/data':
            self.send_response(200)  
            self.send_header('Content-Type', 'application/json')  
            self.end_headers()  
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))  

        elif self.path == '/status':
            self.send_response(200)  
            self.send_header('Content-Type', 'application/json')  
            self.end_headers()  
            status_data = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(status_data).encode('utf-8'))  

        else:
            self.send_response(404)  
            self.send_header('Content-Type', 'application/json')  
            self.end_headers()  
            error_data = {
                "error": "Endpoint not found"
            }
            self.wfile.write(json.dumps(error_data).encode('utf-8'))  

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """
    Runs the HTTP server on port 8000.

    This function sets up the server with the specified address and handler class,
    and starts the server to listen for incoming requests.
    """
    server_address = ('', 8000)  
    httpd = server_class(server_address, handler_class)  
    print('Starting httpd on port 8000...')  
    httpd.serve_forever()  

if __name__ == '__main__':
    """
    This block executes the run function when the script is run directly.

    It initializes and starts the server, allowing it to handle incoming requests.
    """
    run()  
