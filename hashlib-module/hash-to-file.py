import hashlib

a=hashlib.sha512(input("Enter Your string here:").encode()).hexdigest()
f=open('hash.txt',"w")
f.write(a)
f.close()