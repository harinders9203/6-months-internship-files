import hashlib
def stored_pswd():
    pswd=hashlib.sha512("Admin@123".encode()).hexdigest()
    return pswd

a=hashlib.sha512(input("Enter your password:").encode()).hexdigest()
b=stored_pswd()
if a==b:
    print("Password is correct")
else:
    print("Password is incorrect")