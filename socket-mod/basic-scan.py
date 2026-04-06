import socket

target='127.0.0.1'

for port in range(20,101):
    s=socket.socket()
    s.settimeout(1)


    r=s.connect_ex((target,port))

    if r==0:
        print(f"connected to port {port}")
    else:
        print(f"{port} is closed")

    s.close()
