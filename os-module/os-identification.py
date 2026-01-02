import os
#print(os.name)
a=(os.name)
if a=='posix':
    os.system('ifconfig')
else:
    os.system('ipconfig')