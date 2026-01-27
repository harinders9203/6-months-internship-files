import re

p=input("Enter password:")
s=0
si=len(p)
if si < 8:
    print("Password length must be greater then 8")
if re.search("[a-z]",p):
    s+=1
if re.search("[A-Z]",p):
    s+=1
if re.search('[0-9]',p):
    s+=1
if re.search('!@#$%&*()_+',p):
    s+=1

if s<2:
    print("Password is too weak")
elif s<3:
    print("Password is weak")
elif s<4:
    print("Good password")
else:
    print("Password is strong")