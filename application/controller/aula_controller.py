from application import app
from flask import render_template, request
from application.model.entity.aula import Aula
from application.model.dao.aula_dao import AulaDAO

@app.route("/aula")
def aula():
    aula_dao = AulaDAO() 
    return render_template("aula.html", aula_dao=aula_dao)