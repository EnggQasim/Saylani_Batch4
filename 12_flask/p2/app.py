from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Line1</p>\
<p>Line2</p>\
<p>Line2</p>\
"


@app.route("/about")
def about():
    return "<h1>About Saylani</h1><p>Line1</p>\
<p>Line2</p>\
<p>Line2</p>\
"


app.run(debug=True)
