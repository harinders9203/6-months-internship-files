from cryptography.fernet import Fernet
import hashlib
import base64
def encoding():
    msg=input("Enter your secret msg: ").encode()
    key1=input("Enter your secret key: ").encode()
    hashed=hashlib.sha256(key1).digest()
    key=base64.urlsafe_b64encode(hashed)
    cipher=Fernet(key)
    encrypted=cipher.encrypt(msg)
    print(encrypted.decode())
def decoding():
    msg=input("Enter your encrypted msg: ").encode()
    key1=input("Enter your secret key: ").encode()
    hashed=hashlib.sha256(key1).digest()
    key=base64.urlsafe_b64encode(hashed)
    cipher=Fernet(key)
    decr=cipher.decrypt(msg.decode())
    print("Your decrypted text is ",decr)
decoding()