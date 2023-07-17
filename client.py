import socket

DOWNLOAD_FILE_PATH="./Downloads/test.txt"
# HOST = "localhost"
PORT = 9090
try:
    HOST = input("Enter the HOST IP: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    client.connect((HOST, PORT)) #Connect to the server running on localhost

    #Only GET instruction is supported
    while True:
        instruction = input("Enter the operation: ")
        if(instruction=="GET"):
            client.send(instruction.encode())
            break
        else:
            print("Only GET is supported. Try again...")

    #Data buffer
    data = ""
    while True:
        received_data = client.recv(6).decode() #Receive the data sent by the client
        if "<EOF>" in received_data:
            break
        data = data+received_data

    with open(DOWNLOAD_FILE_PATH, "w") as file:
        file.write(data)
        print("Download successful")
    

except Exception as e:
    print("Connection terminated!")
    print(e)
