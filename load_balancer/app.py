# from flask import Flask, request, Response
# import requests
# import logging

# app = Flask(__name__)

# # List of backend servers
# backends = ['http://localhost:5000', 'http://localhost:5001']
# backend_index = 0

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# @app.route('/', methods=['GET', 'POST'])
# def load_balancer():
#     global backend_index
    
#     # Select backend server using round-robin approach
#     backend = backends[backend_index]
#     backend_index = (backend_index + 1) % len(backends)
    
#     logging.info(f"Forwarding request to: {backend}")
    
#     try:
#         # Forward the request to the selected backend server
#         resp = requests.request(
#             method=request.method,
#             url=backend,
#             headers={key: value for (key, value) in request.headers if key != 'Host'},
#             data=request.get_data(),
#             cookies=request.cookies,
#             allow_redirects=False
#         )
        
#         # Return the backend server's response
#         return Response(
#             resp.content,
#             status=resp.status_code,
#             headers=dict(resp.headers)
#         )
    
#     except requests.RequestException as e:
#         logging.error(f"Error forwarding request: {e}")
#         return Response("Error forwarding request", status=500)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=8080)


from flask import Flask, redirect
import requests

app = Flask(__name__)

# Use a round-robin approach
server_index = 0
servers = [
    "http://backend_server_1:5000",  # Use Docker service names
    "http://backend_server_2:5001"
]

@app.route('/')
def load_balance():
    global server_index
    try:
        # Forward request to the appropriate backend server
        response = requests.get(servers[server_index])
        server_index = (server_index + 1) % len(servers)  # Rotate to the next server
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error forwarding request: {e}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
