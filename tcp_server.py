from socket import socket


import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((socket.gethostname(),4040))

server_socket.listen(5)
while True: 
    client_socket, addr=server_socket.accept()
    print("connection from {} has been established!".format(addr))
    data="i love python and blackhat"
    client_socket.send(bytes(data, "utf-8"))
    client_socket.close()