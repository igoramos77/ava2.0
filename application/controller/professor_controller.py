from application import app
from flask import render_template, request

@app.route("/professor/")
def professor():
    return render_template("professor.html")
    