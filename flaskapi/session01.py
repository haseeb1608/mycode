#!/usr/bin/python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import escape
from flask import request

app = Flask(__name__)
app.secret_key = "keyyyyyyyy"

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        return "Logged in as " + username + "<br>" + \
            "<b><a href = '/logout'>click here to log out</a></b>"

    return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":

        session["username"] = request.form.get("username")
        return redirect(url_for("index"))
    return """
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/logout")
def logout():
   # remove the username from the session if it is there
   session.pop("username", None)
   return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2224)

