import hashlib

f=open("hash.txt","r")
pswd=f.read()
rp=hashlib.sha512(input("Enter your Password here:").encode()).hexdigest()
if rp==pswd:
    print("Password is correct...")
else:
    print("Password is incorrect..")