from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/exercises")
def exercises():
    return render_template("index.html")
