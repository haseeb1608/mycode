from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)
@app.route("/login")
@app.route("/")
def index():
    return render_template("login.html")

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            user = 'defaultuser'

        resp = make_response(render_template("readcookie.html"))

        resp.set_cookie("userID", user)

        return resp

    if request.get == "GET":
        return redirect(url_for("index"))

@app.route("/getcookie")
def getcookie():
    # attempt to read the value of userID from user cookie
    name = request.cookies.get("userID") # preferred method

    # name = request.cookies["userID"] # <-- this works but returns error
                                       # if value userID is not in cookie

    # return HTML embedded with name (value of userID read from cookie)
    return f'<h1>Welcome {name}</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

