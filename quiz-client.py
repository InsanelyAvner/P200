import socket
from threading import Thread

# AF_INET is address family, SOCK_STREAM is socket type
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ask an input from user to get their username
nickname = input("Enter your nickname: ")

ip_address = '127.0.0.1'  # Localhost IP address
port = 8000  # Can be any number provided it is not lower than 1024

# Connect our server with the IP and the port
client.connect((ip_address, port))
print("Connected with the server")

# Create a fnction to receive messages
def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))

        except:
            print("An error has occured.")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("Your answer: ")}'
        client.send(message.encode('utf-8'))


receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()