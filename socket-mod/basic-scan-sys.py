import socket
import sys

target=sys.argv[1]

print('Scanning {target}....')

for port in range(21,101):
    s=socket.socket()

    r=s.connect_ex((target,port))
    s.settimeout(1)

    if r==0:
        print(f'{port} is open')
    else:
        print(f'{port} is closed')

    s.close()