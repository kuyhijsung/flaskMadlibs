from flask import Flask
from stories import generate

app = Flask(__name__)


@app.route("/")
def show_home():
    return "Welcome"
