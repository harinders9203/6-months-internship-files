from flask import Flask as f,request,render_template
import sqlite3
app=f(__name__)
@app.route("/log",methods=["GET","POST"])
def log():
    if request.method=="GET":
        return f"Get mt"