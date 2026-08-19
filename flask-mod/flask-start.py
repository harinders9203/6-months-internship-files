from flask import Flask
app=Flask(__name__)
@app.route("/home")
def home():
    return "hello world"

@app.route("/cyber")
def cyber():
    return "Cyber page"


@app.route("/about")
def about():
    return "About"


@app.route("/recv",methods=["GET"])
def recv():
    return "Form received"

@app.route("/log",methods=["POST"])
def log():
    return "info send"

if __name__=="__main__":
    app.run(debug=True)