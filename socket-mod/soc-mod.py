import socket

s=socket.socket() #creating socket

r=s.connect_ex(("127.0.0.1", 80))
# print(r)

if r==0:
    print("Port is open")
else:
    print("Port is closed")

s.close()