import socket
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),4040))

response=client_socket.recv(4090)
print(response.decode("utf-8"))


