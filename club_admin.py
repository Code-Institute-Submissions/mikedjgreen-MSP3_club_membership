# msp3 club membership MDJG 28/10/2020
import os
from flask import Flask, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/", methods=["GET", "POST"])
def membership():
    if request.method == "POST":
        flash("** Thanks {} {}, we have recieved your request **".
              format(request.form.get("forename"),
                     request.form.get("lastname")))
    return render_template("membership.html", page_title="Membership Request")


@app.route("/members")
def members():
    return render_template("members.html",
                           page_title="Members List")


@app.route("/activities")
def activities():
    return render_template("activities.html",
                           page_title="Extra-mural Activities")


@app.route("/exhibition")
def exhibition():
    return render_template("exhibition.html",
                           page_title="Annual Exhibition")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html",
                           page_title="Gallery of Members works")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html",
                           page_title="Administrator Registration")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
