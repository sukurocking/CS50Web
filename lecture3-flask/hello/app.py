from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/greet")
def greet():
    name = request.args.get("name")
    if not name:
        name = "World"
    return render_template("greet.html", name=name)