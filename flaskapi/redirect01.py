from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("log_in.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    # if user sent a POST
    if request.method == "POST":
        # if the POST contains 'admin' as the value for 'username'
        if request.form["username"] == "admin" :
            return redirect(url_for("success")) # return a 302 redirect to /success
        else:
            abort(401)  # if they didn't supply the username 'admin' send back a 401, auth failure
    elif request.method == "GET":
        return redirect(url_for("index")) # if they sent a GET to /login send 302 redirect to /

@app.route("/success")
def success():
    return "logged in successfully"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

