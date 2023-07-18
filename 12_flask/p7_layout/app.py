from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about_students")
def about():
    return render_template("about.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


app.run(debug=True)
