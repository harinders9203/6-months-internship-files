import socket
import sys

target=sys.argv[1]

print('Scanning {target}....')
start=int(sys.argv[2])
end=int(sys.argv[3])

for port in range(start,end+1):
    s=socket.socket()

    r=s.connect_ex((target,port))
    s.settimeout(1)

    if r==0:
        print(f'{port} is open')
        print(f'This uses {socket.getservbyport(port)}')
    else:
        print(port)

    s.close()