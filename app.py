from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    """
    Homepage
    """
    return render_template("homepage.html")


@app.route("/exercises")
def exercises():
    """
    Page with the exercises that will return the FEN
    """
    return render_template("index.html")
