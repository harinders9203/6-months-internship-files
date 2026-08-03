import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 2222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Listening on {PORT}")

while True:
    client, addr = server.accept()
    print(f"[{datetime.now()}] Connection from {addr}")

    client.send(b"SSH-2.0-OpenSSH_8.2\r\n")
    data = client.recv(1024)

    print(data.decode(errors="ignore"))

    client.close()
