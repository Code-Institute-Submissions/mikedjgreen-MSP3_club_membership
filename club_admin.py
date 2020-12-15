"""
   msp3 club membership MDJG 28/10/2020
   This is the main application module for club administration.
"""
import os
import datetime
from pymongo.errors import OperationFailure
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
    """
        This is the default route to display
        a membership applicaton form.
        Server side validation ensures member details
        are accurately recorded from the start.
    """
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
    """
        Club administrators are provided with a list of members.
        The total current membership count is displayed.
    """
    members = mongo.db.members.find()
    member_cnt = mongo.db.members.count_documents({})
    flash("Total Members: {} ".format(member_cnt))
    return render_template("members.html",
                           members=members,
                           page_title="Members List")


# Requires text index on members collection
@app.route("/search", methods=["GET", "POST"])
def search():
    """
        Administrators have a search member based on text entries of:
         firstname, lastname and email address.
        There is an underlying text index to facilitate this search.
    """
    query = request.form.get("memberquery")
    members = list(mongo.db.members.find({"$text": {"$search": query}}))
    members_count = mongo.db.members.count_documents({"$text":
                                                      {"$search":
                                                       query}})
    flash("Members found: {} ".format(members_count))
    return render_template("members.html", members=members)


@app.route("/edit_member/<member_id>", methods=["GET", "POST"])
def edit_member(member_id):
    """
        Once identified, individual members details can be changed.
        Once succesfully changed the user is returned to verify changes.
    """
    if request.method == "POST":
        is_paid = True if request.form.get("paid") else False
        is_guest = True if request.form.get("guest") else False
        is_family = True if request.form.get("family") else False
        is_new = True if request.form.get("newmember") else False
        submit = {
            "firstname": request.form.get("forename"),
            "lastname": request.form.get("lastname"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "bio": request.form.get("bio"),
            "paid": is_paid,
            "family": is_family,
            "newmember": is_new,
            "guest": is_guest,
            "portrait": request.form.get("portrait"),
            "updated_by": session["user"],
            "updated_on": datetime.datetime.now()
        }
        mongo.db.members.replace_one({"_id": ObjectId(member_id)}, submit)
        flash("Member Successfully Updated")

    member = mongo.db.members.find_one({"_id": ObjectId(member_id)})
    return render_template("edit_member.html",
                           member=member,
                           page_title="Edit Member Details")


@app.route("/dues")
def dues():
    """
        Administrators would like a list of members
         whose subscriptions are due to be paid.
        Firstly check that the user logged in can do this.
        There are guests who are on the membership list,
         but they are exempt from annual subscriptions.
    """
    if session["user"]:
        members = mongo.db.members.find({"$and":
                                         [{"paid": False}, {"guest": False}]})
        cnt_dues = mongo.db.members.count_documents({"$and":
                                                    [{"paid": False},
                                                     {"guest": False}]})
        flash("Unpaid member subs due: {} ".format(cnt_dues))
        return render_template("members.html",
                               members=members,
                               page_title="Membership Due List")
    else:
        flash("User not logged in {} ".format(session["user"]))
        return redirect(url_for("login"))


@app.route("/reminder/<member_id>", methods=["GET", "POST"])
def reminder(member_id):
    """
        Calling form that displays identified member whose dues fall.
        Used for calling EmailJS against.
    """
    if request.method == "POST":
        print("Reminder POST")
        newremind = {"$set": {"reminder": datetime.datetime.now()}}
        mongo.db.members.update_one({"_id": ObjectId(member_id)},
                                    newremind)
        return redirect(url_for("members.html"))
    member = mongo.db.members.find_one({"_id": ObjectId(member_id)})
    return render_template("reminder.html",
                           member=member,
                           page_title="Remind Member")

#
#                                   Activities
#


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    """
        A form to enter details of new club activities as events are scheduled.
        Firstly check if user logged in to do this.
    """
    if session["user"]:
        if request.method == "POST":
            activity = {
                "activity_date": request.form.get("activity_date"),
                "description": request.form.get("description"),
                "activity_time": request.form.get("activity_time"),
                "activity_duration": request.form.get("activity_duration"),
                "lead_firstname": request.form.get("lead_firstname"),
                "lead_lastname": request.form.get("lead_lastname"),
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
    """
        Displays a list of the club's forthcoming events.
    """
    activities = mongo.db.activities.find()
    return render_template("activities.html",
                           activities=activities,
                           page_title="Extra-mural Activities")


@app.route("/edit_activity/<activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):
    """
        Once an activity is identified, it can be modified for change in venue,
        date and time, or lead member.
    """
    if request.method == "POST":
        submit = {
            "activity_date": request.form.get("activity_date"),
            "description": request.form.get("description"),
            "activity_time": request.form.get("activity_time"),
            "activity_duration": request.form.get("activity_duration"),
            "lead_firstname": request.form.get("lead_firstname"),
            "lead_lastname": request.form.get("lead_lastname"),
            "activity_image": request.form.get("active_img"),
            "updated_by": session["user"],
            "updated_on": datetime.datetime.now()
        }
        mongo.db.activities.replace_one({"_id": ObjectId(activity_id)}, submit)
        flash("Activity Successfully Updated")

    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    return render_template("edit_activity.html",
                           activity=activity,
                           page_title="Edit Activity Details")


@app.route("/flag_activity/<activity_id>", methods=["GET", "POST"])
def flag_activity(activity_id):
    """
        An interest in an activity can be flagged by member or onlooker.
    """
    if request.method == "POST":
        is_member = True if request.form.get("member") else False
        query = {"_id": ObjectId(activity_id)}
        person = {"firstname": request.form.get("firstname"),
                  "lastname": request.form.get("lastname"),
                  "member": is_member,
                  "email": request.form.get("email"),
                  "interest_flagged": datetime.datetime.now()}
        flag = {"$addToSet": {"interest": person}}
        mongo.db.activities.update_one(query, flag)
        flash("Activity Flagged for you")
        return redirect(url_for("activities"))

    activity = mongo.db.activities.find_one({"_id": ObjectId(activity_id)})
    return render_template("flag_activity.html",
                           activity=activity,
                           page_title="Flag Interest in Activity")

#
#                                   Exhibition
#


@app.route("/add_exhibition", methods=["GET", "POST"])
def add_exhibition():
    """
        Entry of the next summer exhibition details starts here.
        Firstly check if user logged in to do  this
    """
    if session["user"]:
        if request.method == "POST":
            exhibition = {
                "year": request.form.get("year"),
                "location": request.form.get("location"),
                "start_date": request.form.get("start_date"),
                "end_date": request.form.get("end_date"),
                "added_by": session["user"],
                "added_on": datetime.datetime.now()
            }
            flash("** Thanks {}, exhibition added **".format(session["user"]))
            mongo.db.exhibition.insert_one(exhibition)
    else:
        flash("User not logged in to do this")
        return redirect(url_for("login"))
    return render_template("add_exhibition.html", page_title="Add Exhibition")


@app.route("/exhibition")
def exhibition():
    """
        Displays details of the clubs forthcomming exhibition(s).
    """
    exhibition = mongo.db.exhibition.find()
    return render_template("exhibition.html",
                           exhibition=exhibition,
                           page_title="Annual Exhibition")


#
#                                   Gallery
#


@app.route("/gallery")
def gallery():
    """
        Displays a 'gallery' of members works
    """
    gallery = mongo.db.gallery.find()
    artworks = mongo.db.artworks.find()
    return render_template("gallery.html",
                           gallery=gallery,
                           artworks=artworks,
                           page_title="Gallery of Members works")


@app.route("/add_gallery", methods=["GET", "POST"])
def add_gallery():
    """
        A gallery entry details is recorded here.
        Firstly check if user logged in to do  this
    """
    if session["user"]:
        if request.method == "POST":
            gallery = {
                "year": request.form.get("year"),
                "added_by": session["user"],
                "added_on": datetime.datetime.now()
            }
            flash("** Thanks {}, Gallery entry added **"
                  .format(session["user"]))
            mongo.db.gallery.insert_one(gallery)
    else:
        flash("User not logged in to do this")
        return redirect(url_for("login"))
    return render_template("gallery.html", page_title="Add Gallery")


@app.route("/edit_gallery/<gallery_id>", methods=["GET", "POST"])
def edit_gallery(gallery_id):
    """
        A particular gallery entry being identified, it can be modified.
        Firstly check if user logged in to do this
    """
    if session["user"]:
        submit = {
            "year": request.form.get("year"),
            "updated_by": session["user"],
            "updated_on": datetime.datetime.now()
        }
        flash("** Thanks {}, Gallery entry edited **"
              .format(session["user"]))
        mongo.db.gallery.replace_one({"_id": ObjectId(gallery_id)},
                                     submit)
    else:
        flash("User not logged in to do this")
        return redirect(url_for("login"))
    gallery = mongo.db.gallery.find_one({"_id": ObjectId(gallery_id)})
    return render_template("edit_gallery.html",
                           gallery=gallery,
                           page_title="Edit Gallery Details")


@app.route("/add_artwork/<gallery_id>", methods=["GET", "POST"])
def add_artwork(gallery_id):
    """
        Within a gallery entry an art work can be added.
        Firstly check if user logged in to do  this
    """
    if session["user"]:
        if request.method == "POST":
            artwork = {
                "artist": request.form.get("artist"),
                "title": request.form.get("title"),
                "media": request.form.get("media"),
                "height": request.form.get("height"),
                "width": request.form.get("width"),
                "image": request.form.get("image"),
                "price": request.form.get("price"),
                "sold": request.form.get("sold"),
                "added_by": session["user"],
                "added_on": datetime.datetime.now()
            }
            try:
                artstub = mongo.db.artworks.insert_one(artwork)
            except OperationFailure:
                raise OperationFailure("Failure to add an artwork")
            except Exception as e:
                return e
            """
            Once artwork added, need to record id within Gallery's
            artworks array
            """
            try:
                mongo.db.gallery.update_one({"_id": ObjectId(gallery_id)},
                                            {"$addToSet": {"artworks":
                                                          {"art_id": (
                                             ObjectId(artstub.inserted_id)),
                                             "artist": (
                                                 request.form.get("artist")),
                                             "title": (
                                                 request.form.get("title")),
                                             "media": (
                                                 request.form.get("media")),
                                             "height": (
                                                 request.form.get("height")),
                                             "width": (
                                                 request.form.get("width")),
                                             "image": (
                                                 request.form.get("image")),
                                             "price": (
                                                 request.form.get("price")),
                                             "sold": (
                                                 request.form.get("sold")),
                                             "added_by": (
                                                 session["user"]),
                                             "added_on": (
                                                 datetime.datetime.now())}
                                            }})
            except OperationFailure:
                raise OperationFailure("Failure to add an artwork to gallery")
            except Exception as e:
                return e
            flash("** Thanks {}, art work entry added **"
                  .format(session["user"]), category="message")
    else:
        flash("User not logged in to do this")
        return redirect(url_for("login"))
    return redirect(url_for("gallery"))


@app.route("/edit_artwork/<art_id>", methods=["GET", "POST"])
def edit_artwork(art_id):
    """
        Within a gallery entry an art work has been selected.
        A change to the entry's details is needed.
        Firstly check if user logged in to do  this
    """
    if session["user"]:
        if request.method == "POST":
            submit = {"_id": ObjectId(art_id),
                      "artist": request.form.get("artist"),
                      "title": request.form.get("title"),
                      "media": request.form.get("media"),
                      "height": request.form.get("height"),
                      "width": request.form.get("width"),
                      "image": request.form.get("image"),
                      "price": request.form.get("price"),
                      "sold": request.form.get("sold"),
                      "amended_by": session["user"],
                      "amended_on": datetime.datetime.now()}
            mongo.db.artworks.update({"_id": ObjectId(art_id)},
                                     {"$set": submit})
            flash("** Thanks {}, art work amended **".format(session["user"]))
        try:
            artworks = mongo.db.artworks.find_one({"_id": ObjectId(art_id)})
        except OperationFailure:
            raise OperationFailure("Failure to find artwork")
        except Exception as e:
            return e
        year = datetime.datetime.year()
        return render_template("edit_artwork.html",
                               artworks=artworks,
                               year=year,
                               page_title="Edit Artwork Details")
    else:
        flash("User not logged in to do this")
        return redirect(url_for("login"))
    return redirect(url_for("gallery"))


@app.route("/delete_artwork/<art_id>")
def delete_artwork(art_id):
    """
        Within a gallery entry an art work can be deleted.
        Firstly check if user logged in to do this
    """
    if session["user"]:
        mongo.db.gallery.update_one({}, (
            {"$pull": {"artwork": {"art_id": ObjectId(art_id)}}}))
        flash("** Thanks {}, art work deleted **".format(session["user"]))
    else:
        flash("User not logged in to do this")
        return redirect(url_for("login"))
    return redirect(url_for("gallery"))


#
#                                   Register  users
#


@app.route("/register", methods=["GET", "POST"])
def register():
    """
        Entry of new users (administrators) .
    """
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
    """
        Login form, checking user exists and has entered correct password.

    """
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
    """
        Remove user from session cookie.
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/users")
def users():
    """
        Lists current users of  the club database
    """
    users = mongo.db.users.find()
    return render_template("users.html",
                           users=users,
                           page_title="List of usernames")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
