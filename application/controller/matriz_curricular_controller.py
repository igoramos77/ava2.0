from application import app
from application.model.dao.periodo_dao import PeriodoDAO
from flask import render_template, request
from application.model.entity.periodo import Periodo

@app.route("/matriz-curricular")
def matriz_curricular():
    periodo_dao = PeriodoDAO()
    periodo_list = periodo_dao.listar_todos()
    return render_template("matriz_curricular.html", periodo_list=periodo_list)
