# ftp-python
Simple FTP client and server using Python. I call it  PyFiTP :)

# Usage
Clone the repository and open up up your terminal in 'ftp-python' directory. Now execute the following command<br>
```
python3 server.py
```
or, if you are on windows
```
python server.py
```
Your very own FTP server will start<br>
Then open up another terminal, either in the same computer or in a different computer and type in the following command to start the client<br>
```
python3 client.py
```
or, if you are on windows
```
python server.py
```
Now that you have a client running, type in the IP address of the server(192.168.X.X) and connect to the server. You will see a connection message in the server's terminal. As of now, you can send "GET" instruction to download a text file from ./data

# Limitations
- It will work only on text files and nothing else
- Multiple clients are not supported
- Only GET instruction is present to download a text file
