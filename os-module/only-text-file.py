import os

p=input("Enter the path to check: ")
w=os.listdir(p)
for f in w:
    if(f.endswith('.txt')):
        print(f)
