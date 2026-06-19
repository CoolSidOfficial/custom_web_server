import socket
from verabose import make_response

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen()

print("Server running on http://localhost:8080")

while True:
    client, addr = server.accept()

    request = client.recv(1024).decode()

    if not request:
        client.close()
        continue

    first_line = request.split("\r\n")[0]

    method = first_line.split(" ")[0]
    path = first_line.split(" ")[1]

    parts = request.split("\r\n\r\n")
    body = parts[1] if len(parts) > 1 else ""

    print(f"Method: {method}")
    print(f"Path: {path}")
    print(f"Body: {body}")
    print("-" * 50)

    if method == "GET" and path == "/":
        response = make_response("<h1>Home Page</h1>")

    elif method == "GET" and path == "/about":
        response = make_response("<h1>About Page</h1>")

    elif method == "POST" and path == "/login":
        response = make_response(
            f"""
            <h1>Login Received</h1>
            <p>{body}</p>
            """
        )

    else:
        response = make_response("<h1>404 Not Found</h1>")

    client.sendall(response.encode())
    client.close()