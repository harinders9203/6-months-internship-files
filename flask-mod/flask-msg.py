from flask import Flask,request,render_template
from cryptography.fernet import Fernet
import base64
import hashlib



app=Flask(__name__)
@app.route("/msg",methods=["GET","POST"])
def msg():
    if request.method=="GET":
        return render_template("msg.html")
    if request.method=="POST":
        msg=request.form["msg"]
        key=request.form["key"]
        encrypted = encoding(msg, key)
        # decrypted = decoding(msg,key)
        ch=request.form["choice"]
        if ch=="enc":
            result=encoding(msg,key)
            return render_template("msg.html",encrypted=result.decode())

        elif ch=="dec":
            result=decoding(msg,key)
            return render_template("msg.html",decrypted=result.decode())



def encoding(msg,key):
    m=msg.encode()
    k1=hashlib.sha256(key.encode()).digest()
    k=base64.urlsafe_b64encode(k1)
    cipher=Fernet(k)
    encrypted=cipher.encrypt(m)

    return encrypted

def decoding(msg,key):
    m=msg.encode()
    k1=hashlib.sha256(key.encode()).digest()
    k=base64.urlsafe_b64encode(k1)
    cipher=Fernet(k)
    decrypted=cipher.decrypt(m)

    return decrypted



if __name__=="__main__":
    app.run(debug=True)