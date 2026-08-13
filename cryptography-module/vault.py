from cryptography.fernet import Fernet

print(f"=====Secret Vault=====")

ch=input("1.Encrypt msg \n2.Dcrypt msg\nEnter choice: ")
if ch=="1":
    msg=input("Enter msg: ").encode()
    key=Fernet.generate_key()
    obj=Fernet(key)
    cipher_text=obj.encrypt(msg)
    print(f"Here's your key: {key}")
    print(f"Here's your encryted msg: {cipher_text}")
    print("Keep in mind don't forget the key.....")
elif ch=="2":
    msg=input("Enter your Encrypted msg: ").encode()
    key=input("Enter your key: ").encode()
    obj=Fernet(key)
    encrypted_text=obj.decrypt(msg).decode()
    print(f"Your Decrypted msg is: {encrypted_text}")
    print("Thanks for using....")
else:
    print("Please enter the correct choice.....")