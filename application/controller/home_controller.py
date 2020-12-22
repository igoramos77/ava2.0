from application import app
from application.model.dao.disciplina_dao import DisciplinaDAO
from application.model.entity.disciplina import Disciplina
from flask import render_template, request, session

@app.route("/")
@app.route("/dashboard")
def dashboard():
    disciplina_dao = DisciplinaDAO()
    disciplina_list = disciplina_dao.listar_todos()

    today = disciplina_dao.today

    assessments = disciplina_dao.assessments
    jobs = disciplina_dao.jobs
    foruns = disciplina_dao.foruns
    production = disciplina_dao.production

    session['aluno_logado'] = {
        'nome': 'Igor Brown',
        'email': 'igorbrownramos@gmail.com',
        'avatar': None or 'avatar.svg'
    }

    return render_template("dashboard.html",
        disciplina_list=disciplina_list, 
        today=today,
        assessments=assessments,
        jobs=jobs,
        foruns=foruns,
        production=production
    )