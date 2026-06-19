import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",8080))
server.listen()
print("Listening on 8080 port")
client_socket,address=server.accept()
print(f"connected by {address}")
client_socket.close()
server.close()

