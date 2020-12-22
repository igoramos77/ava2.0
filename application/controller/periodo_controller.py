from application import app
from application.model.dao.periodo_dao import PeriodoDAO
from flask import render_template, request

@app.route("/periodo")
def periodo():
    periodo_id = request.args.get('numero')
    if periodo_id is None:
        periodo_id = 1
    periodo = PeriodoDAO().buscar_por_id(int(periodo_id))
    return render_template("periodo.html", periodo=periodo)