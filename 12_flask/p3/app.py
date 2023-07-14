from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
<h1>Saylani Mass IT program</h1>
<h2>Home Page</h2>
"""


app.run(debug=True)
