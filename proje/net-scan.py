import socket
import threading
import sys


def scan(target,start,stop):
    f=False
    for port in range(start, stop):
        s=socket.socket()
        s.settimeout(1)
        r=s.connect_ex((target, port))
        if r==0:
            print(f'port is opened and using {port} with service {socket.getservbyport(port)}')
            True
        s.close()
    if f==False:
        print("No open ports found")


t=[]
target=sys.argv[1]
start=int(sys.argv[2])
end=int(sys.argv[3])

for i in range(start, end):
    th=threading.Thread(target=scan, args=(target,start,end))
    t.append(th)
    th.start()

for th in t:
    th.join()

scan(target=target,start=start,stop=end)
