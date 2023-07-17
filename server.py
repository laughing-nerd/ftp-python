import socket

FILE_PATH = "./data/test.txt"
HOST = ""
PORT = 9090
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT)) #Only localhost clients can connect to this server
    server.listen(1) #Listen for incoming connections
    print(f"Server is listening on port {PORT}")

    while True:
        client, addr = server.accept(); #Catch the incoming connection
        print(f"{addr} is now connected to me!")

        instruction = client.recv(3).decode() #Receive instruction from the client. Currently only GET is supported
        
        if(instruction=="GET"):
            with open(FILE_PATH, "r") as file:
                data = file.read()
            data = data+"<EOF>"
            client.sendall(data.encode())
            print("Sent file to the client")

except Exception as e:
    print("Connection terminated!")
    print(e)

