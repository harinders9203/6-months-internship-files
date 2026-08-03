import re
def strength(passw):
    l=len(passw)
    s=0
    if l<8:
        print("Password must be more then 8 characters")

    if re.search("[A-Z]",passw):
        s+=1
    if re.search("[a-z]",passw):
        s+=1
    if re.search("[0-9]",passw):
        s+=1
    if re.search("[!@#$%^&*()_+]",passw):
        s+=1

    if s == 5:
        return "Very Strong Password"
    elif s == 4:
        return "Strong Password"
    elif s == 3:
        return "Medium Password"
    else:
        return "Weak Password"



p=input("Enter password:")
print(strength(p))