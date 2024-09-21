import socket
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 65535


nickname = input('Enter your nickname: ')

client_socket = socket.socket()
client_socket.connect((SERVER_IP, SERVER_PORT))


def write():
    while True:
        message = f"{nickname} -> {input()}"
        client_socket.send(message.encode())


def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == 'Nickname':
                client_socket.send(nickname.encode())
            else:
                print(message)

        except:
            client_socket.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()