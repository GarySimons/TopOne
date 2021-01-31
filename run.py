import os
from flask import Flask, render_template

app = Flask(__name__)

# app route for home page
@app.route("/")
def index():
    return render_template("index.html")


# app route for about page
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=(os.environ.get("PORT")),
        debug=False)