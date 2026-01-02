import re
pswd=input(("Enter the password:"))

if not re.search('^[A-Za-z0-9]',pswd):
    print("Password doen't include special character..")
else:
    print("Strong password")