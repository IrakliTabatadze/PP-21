import socket

HOST = '127.0.0.1'
PORT = 65434


with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))

    message = b'Hello, Server!!!'

    print(message)

    client_socket.send(message)

    data = client_socket.recv(1024).decode('utf-8')


    print(data)
