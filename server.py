import socket
import threading 

FILE_PATH = "./data/test.txt"
HOST = ""
PORT = 9090

def handleConnections(client, addr):
    print(f"{addr} is now connected to me!")
    
    instruction = client.recv(3).decode() #Receive instruction from the client. Currently only GET is supported
       
    if(instruction=="GET"):
        with open(FILE_PATH, "r") as file:
            data = file.read()
            data = data+"<EOF>"
        client.sendall(data.encode())
        print(f"File sent to {addr}")

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5) #Listen for incoming connections
    print(f"Server is listening on port {PORT}")

    while True:
        client, addr = server.accept(); #Catch the incoming connections
        thread = threading.Thread(target=handleConnections, args=(client, addr))
        thread.start()
        
except Exception as e:
    print("Connection terminated!")
    print(e)

