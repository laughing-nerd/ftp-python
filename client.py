import socket

HOST=""
PORT=9090

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = input("Enter the IP to connect: ")
    client.connect((HOST,PORT))
    while True:
        data = client.recv(1024).decode()
        print(data)
except Exception as err:
    print("Connection terminated!")
    print(err)
