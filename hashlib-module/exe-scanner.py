import hashlib
import os
import re

n=input("Enter file name/path here:")
if n.endswith(".exe"):
    if os.path.isfile(n):
        f=open(n,'rb')
        hs=f.read()
        he=hashlib.sha256(hs).hexdigest()
        f.close()
        print(he)
    else:
        print("No file founded..")
else:
    print("only exe files are allowed")