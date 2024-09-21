import socket
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 65535

server_socket = socket.socket()
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print(f"Server is listening to port {SERVER_PORT}")

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat!!!".encode('utf-8'))
            nicknames.remove(nickname)
            client.close()
            break

def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected With {str(address)}")

        client.send("Nickname".encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print(f'{nickname} connected to the chat')
        broadcast(f"{nickname} has joined the chat!!!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()