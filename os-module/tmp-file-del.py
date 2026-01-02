import os

p='.'
h=[]
f=os.listdir(p)
for fil in f:
    if(fil.endswith(".tmp")):
        h.append(fil)
        os.remove(fil)

print(f"The deleted files are:\n{h}")