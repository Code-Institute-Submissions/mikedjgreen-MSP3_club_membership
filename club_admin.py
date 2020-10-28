# msp3 club membership MDJG 28/10/2020
import os
from flask import Flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
def Hello():        # Test Flask works
    return "Hello World...again!"   # Test message


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
