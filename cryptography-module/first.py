from cryptography.fernet import Fernet
key=Fernet.generate_key() #for key generation
cipher=Fernet(key)
msg=input("Enter message you want to encrypt:").encode()

encrypt=cipher.encrypt(msg)
print(f"Your msg: {msg}\nYour key:{key}\nYour encrypted msg:{encrypt} ")

# a=open("test.txt",'a')
# a.write(f"key: {key}\nEncrypted:{encrypt} \n")
# a.close()






# for decryption
key1=input("Enter key: ").encode()
cipher=Fernet(key1)
encrypted_text=input("Enter the encrypted text: ").encode()
dec=cipher.decrypt(encrypted_text)
print(dec)