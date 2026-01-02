import os
n=input("Enter the name of the file:")
if os.path.exists(n):
    print("Sensitive file found.")
else:
    print("file doesn't exists")