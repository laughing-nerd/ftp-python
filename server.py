import socket
import threading

HOST=""
PORT=9090
CONNECTIONS=[]

UNICAST_MESSAGE = "This is a unicast message and is sent to the first client that connected to this server"
MULTICAST_MESSAGE = "This is a multicast message and is sent to n/2 clients connected to this server; where n is the number of total connections"
BROADCAST_MESSAGE = "This is a broadcast message and is sent to all the clients connected to this server"

def thread_connection():
    while True:
        client, addr = server.accept()
        print(f"\n{addr} connected to the server")
        CONNECTIONS.append((client, addr))

def server_connection():
    while True:
        instruction = input("instruction: ")
        if(instruction == "UNI"):
            if(len(CONNECTIONS)!=0):
                CONNECTIONS[0][0].send(UNICAST_MESSAGE.encode())
            else:
                print("No clients are connected...")
        elif(instruction == "BRD"):
            if(len(CONNECTIONS)!=0):
                for CONNECTION in CONNECTIONS:
                    CONNECTION[0].send(BROADCAST_MESSAGE.encode())
            else:
                print("No clients are connected...")
        elif(instruction == "MUL"):
            if(len(CONNECTIONS)!=0):
                for i in range(0,len(CONNECTIONS)//2):
                    CONNECTIONS[i][0].send(MULTICAST_MESSAGE.encode())
            else:
                print("No clients are connected...")
        elif(instruction == "LST"):
            if(len(CONNECTIONS)!=0):
                i=1
                for CONNECTION in CONNECTIONS:
                    print(f"{i}. {CONNECTION[1]}")
                    i+=1
            else:
                print("No clients are connected...")

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen(5)
    print(f"Server started on port {PORT}")
    thread1 = threading.Thread(target=thread_connection)
    thread2 = threading.Thread(target=server_connection)
    thread1.start()
    thread2.start()

except Exception as err:
    print("Connection terminated!")
    print(err)

