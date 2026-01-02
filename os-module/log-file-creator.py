import os
n=input("enter the name:")
if os.path.exists(f'{n}.log'):
    f=open(f'{n}.log','r')
    print(f.read())
else:
    f=open(f'{n}.log','w')
    d=input("Enter the content:")
    f.write(d)
    f.close()
    f=open(f'{n}.log','r')
    print(f.read())