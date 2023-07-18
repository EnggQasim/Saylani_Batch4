from flask import Flask

app = Flask(__name__)


@app.route("/<user_name>")
def index(user_name):
    return "Hello Dear, " + user_name


app.run(debug=True)
