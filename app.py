from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_prompts():
    prompts = story.prompts

    return render_template("questions_form.html", prompts=prompts)


@app.route("/story")
def display_story():

    text = story.generate(request.args)

    return render_template("story.html", text=text)
