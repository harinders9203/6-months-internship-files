import os

name=input("Enter the directory name:")
if os.path.exists(name):
    f=os.listdir(name)
    print(f)
else:
    print("Patha/directory isn't exist")