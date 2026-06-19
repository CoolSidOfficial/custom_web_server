import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",8080))
server.listen()
print("Server running on http://localhost:8080")
while True:
    client,addr=server.accept()
    request=client.recv(1024).decode()
    print(request)
    response = (
                "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html\r\n"
                        "\r\n"
                            "<h1>Hello World</h1>"
                            )

    client.send(response.encode())
    client.close()


