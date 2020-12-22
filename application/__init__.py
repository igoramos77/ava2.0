from flask import Flask
from flask_session import Session
import os
app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))

app.secret_key = '7777777'
app.config['SESSION_TYPE'] = 'filesystem'

from application.controller import home_controller
from application.controller import disciplina_controller
from application.controller import professor_controller
from application.controller import aula_controller

from application.controller import matriz_curricular_controller
from application.controller import periodo_controller