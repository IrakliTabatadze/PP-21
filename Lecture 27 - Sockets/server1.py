
import socket

# HOST = '0.0.0.0'
HOST = '127.0.0.1'
PORT = 65434


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen()
    print(f"Server Socket is Listening To Port {PORT}")

    connection, client_address = server_socket.accept()

    print(f"Client Connected By: {client_address}")

    while True:
        data = connection.recv(1024)
        data = data.decode('utf-8')
        print(f"Received From Client: {data}")

        message = f"Message Received: '{data}', \nThank You!"

        connection.send(message.encode('utf-8'))
