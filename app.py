from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "test123"

debug = DebugToolbarExtension(app)


@app.route("/")
def render_home():
    questions = story.prompts
    return render_template("form.html", questions=questions)


@app.route("/story")
def render_story():
    madlibs = story.generate(request.args)
    return render_template("madlibs.html", madlibs=madlibs)
