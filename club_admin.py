# msp3 club membership MDJG 28/10/2020
import os
from flask import (Flask, render_template,
                redirect, request,
                flash, url_for, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
COLLECTION = "users"


mongo = PyMongo(app)


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
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username {} already exists".format(request.form.get("username")))
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration of {} Successful!".format(request.form.get("username")))
    return render_template("register.html",
                            page_title="Administrator Registration")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
