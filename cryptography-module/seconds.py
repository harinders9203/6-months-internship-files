from cryptography.fernet import Fernet
k=Fernet.generate_key()
f=Fernet(k)
e=f.encrypt(b'hello')
print(e)