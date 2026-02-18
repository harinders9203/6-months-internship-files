import hashlib
import re
p=input("Enter the password: ")
s=0
flg=False
salt="Agoodalt"
if len(p)<8:
    print("The password length should be greater then 8.")
else:
    if re.search('[A-Z]',p):
        s+=1
    if re.search('[a-z]',p):
        s+=1
    if re.search('[0-9]',p):
        s+=1
    if re.search('[!@#$%^&*()_+|]',p):
        s+=1

if s==1:
    print("Password is too weak")
elif s==2:
    print("Password is weak")
elif s==3:
    print("Password is good")
else:
    print("Password is strong now you can move further")

if s!=4:
    exit()

cb=salt+p
ph=hashlib.sha256(cb.encode()).hexdigest()

f=open('pass.txt','a')
f.write(ph+'\n')
f.close()

f=open('pass.txt',"r")


ps=input("Enter Correct password:")
psh=salt+ps
ps=hashlib.sha256(psh.encode()).hexdigest()
f=open('pass.txt','r')
psl=f.readlines()
for i in psl:
    if i.strip()==ps:
        print("Password is correct")
        flg=True
        break
if flg==False:
    print("Password is incorrect")
