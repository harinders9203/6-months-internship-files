import re
import hashlib
from cryptography.fernet import Fernet
from flask import Flask,request,render_template
import base64
import sqlite3

app=Flask(__name__)

@app.route("/notes",methods=["POST","GET"])
def notes():
    if request.method=="GET":
        return render_template("notes.html")
    if request.method=="POST":
        m=request.form["msg"]
        k=request.form["key"]
        r=request.form["choice"]

        if r=='store':
            k=encoding(m,k)
            return f"<script>alert('Your msg is saved in the notes.txt please remember the key')</script>"

        elif r=='read':
            k=decoding(m,k)
            return f"<script>alert('your msg is decrypted: {k}')</script>"



def encoding(msg,key):
    m=msg.encode()
    h=hashlib.sha256(key.encode()).digest()
    k=base64.urlsafe_b64encode(h)
    cipher=Fernet(k)
    encrypted=cipher.encrypt(m)
    en=encrypted.decode()
    a=open("notes.txt",'a')
    a.write(f"\n{en}\n")
    a.close()

    return f"<script>alert('Your notes are save in notes.txt') </script>"


def decoding(msg,key):
    m=msg.encode()
    h=hashlib.sha256(key.encode()).digest()
    k=base64.urlsafe_b64encode(h)
    cipher=Fernet(k)
    decrypted=cipher.decrypt(m)
    dec=decrypted.decode()

    return dec


if __name__=="__main__":
    app.run()
