import socket
from verabose import make_response

if __name__=="__main__":

 server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 server.bind(("localhost",8080))
 server.listen()
 print("Server running on http://localhost:8080")
 while True:
    client,addr=server.accept()
    request=client.recv(1024).decode()
    first_line = request.split("\r\n")[0]
    path = first_line.split(" ")[1]
    
    if path == "/":
        response = make_response("<h1>Home Page</h1>")

    elif path == "/about":
        response = make_response("<h1>About Page</h1>")

    else:
        response = make_response("<h1>404 Not Found</h1>")

    client_socket.sendall(response.encode())
    print(request)
    client.sendall(response.encode())
    client.close()
