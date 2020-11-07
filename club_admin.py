# msp3 club membership MDJG 28/10/2020
import os
import datetime
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
#
#                                   Membership
#


@app.route("/", methods=["GET", "POST"])
def membership():
    if request.method == "POST":
        # check if member's email already exists in db
        existing_member = mongo.db.members.find_one(
            {"email": request.form.get("email").lower()})

        if existing_member:
            flash("Email {} already exists".format(
                request.form.get("email")))
            return redirect(url_for("login"))

        flash("** Thanks {} {}, we have received your request **".
              format(request.form.get("forename"),
                     request.form.get("lastname")))

        member = {
            "firstname": request.form.get("forename"),
            "lastname": request.form.get("lastname"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "newmember": "true",
            "paid": "false",
            "requested_on": datetime.datetime.now()
        }
        mongo.db.members.insert_one(member)

    return render_template("membership.html", page_title="Membership Request")


@app.route("/members")
def members():
    members = mongo.db.members.find()
    return render_template("members.html",
                           members=members,
                           page_title="Members List")


@app.route("/dues")
def dues():
    # check if user logged in to do  this
    if session["user"]:
        members = mongo.db.members.find({"$and":
                                         [{"paid": False}, {"guest": False}]})
        return render_template("members.html",
                               members=members,
                               page_title="Membership Due List")
    else:
        flash("User not logged in {} ".format(session["user"]))
        return redirect(url_for("login"))
#
#                                   Activities
#


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    # check if user logged in to do  this
    if session["user"]:
        if request.method == "POST":
            activity = {
                "activity_date": request.form.get("activity_date"),
                "description": request.form.get("description"),
                "activity_time": request.form.get("activity_time"),
                "activity_duration": request.form.get("activity_duration"),
                "lead_member_firstname": request.form.get("lead_member_firstname"),
                "lead_member_lastname": request.form.get("lead_member_lastname"),
                "added_by": session["user"],
                "added_on": datetime.datetime.now()
            }
            flash("** Thanks {}, activity added **".format(session["user"]))
            mongo.db.activities.insert_one(activity)
    else:
        flash("User not logged in to do this")
        return redirect(url_for("login"))
    return render_template("add_activity.html", page_title="Add Activity")


@app.route("/activities")
def activities():
    activities = mongo.db.activities.find()
    return render_template("activities.html",
                           activities=activities,
                           page_title="Extra-mural Activities")


#
#                                   Exhibition
#


@app.route("/exhibition")
def exhibition():
    exhibition = mongo.db.exhibition.find()
    return render_template("exhibition.html",
                           exhibition=exhibition,
                           page_title="Annual Exhibition")


#
#                                   Gallery
#


@app.route("/gallery")
def gallery():
    gallery = mongo.db.gallery.find()
    return render_template("gallery.html",
                           gallery=gallery,
                           page_title="Gallery of Members works")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username {} already exists".format(
                request.form.get("username")))
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "readonly": request.form.get("group1").lower(),
            "registered_on": datetime.datetime.now()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration of {} Successful!".format(
                        request.form.get("username")))
    return render_template("register.html",
                           page_title="Administrator Registration")


@app.route("/login", methods=["GET", "POST"])
def login():
    usnm = ""
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                            "members", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html",
                           user_name=usnm,
                           page_title="Administrator Login")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/users")
def users():
    users = mongo.db.users.find()
    return render_template("users.html",
                           users=users,
                           page_title="List of usernames")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
