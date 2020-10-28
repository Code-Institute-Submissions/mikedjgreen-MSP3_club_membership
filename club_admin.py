# msp3 club membership MDJG 28/10/2020
import os
from flask import Flask, render_template
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
def membership():
    return render_template("membership.html")


@app.route("/members")
def members():
    return render_template("members.html")


@app.route("/activities")
def activities():
    return render_template("activities.html")


@app.route("/exhibition")
def exhibition():
    return render_template("exhibition.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
