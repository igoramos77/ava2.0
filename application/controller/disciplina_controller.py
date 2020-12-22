from application import app
from application.model.entity.disciplina import Disciplina
from application.model.entity.aula import Aula
from application.model.dao.disciplina_dao import DisciplinaDAO
from application.model.dao.aula_dao import AulaDAO
from flask import render_template, request

@app.route("/disciplina/<int:disciplina_id>")
def disciplina(disciplina_id):
    disciplina_dao = DisciplinaDAO()    
    disciplina = disciplina_dao.buscar_por_id(int(disciplina_id))
    
    aula_dao = AulaDAO()
    aula_list = aula_dao.listar_todas_da_disciplina(int(disciplina_id))


    return render_template("disciplina.html", disciplina=disciplina, aula_list=aula_list)