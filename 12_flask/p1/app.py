from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Saylani DataScience Batch4</h1><p>Hello world!</p>"


app.run(debug=True)
