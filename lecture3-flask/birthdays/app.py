import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
import logging

logging.basicConfig(level=logging.DEBUG)


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name_to_add = request.form.get("name")
        month_to_add = request.form.get("month")
        day_to_add = request.form.get("day")
        logging.debug(f"Name: {name_to_add}, Month: {month_to_add}, Day: {day_to_add}")
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?);", name_to_add,month_to_add, day_to_add)
        return redirect("/")

    else:
        birthdays_list_of_dict = db.execute("select id, name, month, day from birthdays")
        return render_template("index.html", persons=birthdays_list_of_dict)


