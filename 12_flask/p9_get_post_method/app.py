from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/order", methods=["GET"])
def info():
    return "Hello Dear " + request.args.get("user_name") +\
        "Your Email address is : " + request.args.get("email")


@app.route("/login", methods=['POST'])
def login():
    return f"Hell Dear {request.form['user']} Thanks for using our paid services! your password is {request.form['psw']}"


app.run(debug=True)
