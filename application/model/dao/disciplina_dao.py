from application.model.entity.periodo import Periodo
from application.model.entity.disciplina import Disciplina
from application.model.dao.professor_dao import ProfessorDAO

from datetime import datetime

class DisciplinaDAO():
    def __init__(self):
        professorDao = ProfessorDAO()
        self.disciplinas = [
            Disciplina(1, 'Lab. Empreed. e Inovação IV', professorDao.buscar_por_id(1), 4, 'Segunda-feira', '19:00 - 22:00'),  
            Disciplina(2, 'Legislação Aplic. à Informática', professorDao.buscar_por_id(4), 4, 'Terça-feira', '19:00 - 22:00'),  
            Disciplina(3, 'Lab. De Prog. De Interface', professorDao.buscar_por_id(2), 4, 'Quarta-feira', '19:00 - 22:00'),  
            Disciplina(4, 'Gestão Estratégica De Pessoas', professorDao.buscar_por_id(5), 4, 'Quinta-feira', '19:00 - 22:00'),  
            Disciplina(5, 'Gestão Ambiental', professorDao.buscar_por_id(6), 4, 'Sexta-feira', '19:00 - 22:00'),  
            Disciplina(6, 'Modelagem de Banco de Dados I', professorDao.buscar_por_id(3), 4, 'Sábado', '19:00 - 22:00'),
        ]

        self._disciplina_list = []
        self._disciplina_list.append(Disciplina)

        # GET WEEKDAY
        self.today = datetime.today().weekday()
        if self.today == 0:
            self.today = "Segunda-feira"
        if self.today == 1:
            self.today = "Terça-feira"
        if self.today == 2:
            self.today = "Quarta-feira"
        if self.today == 3:
            self.today = "Quinta-feira"
        if self.today == 4:
            self.today = "Sexta-feira"
        if self.today == 5:
            self.today = "Sábado"
        if self.today == 6:
            self.today = "Domingo"

        self.assessments = 11
        self.jobs = 10
        self.foruns = 25
        self.production = 88
        
        
    def listar_todos(self):
        return self.disciplinas
        

    def buscar_por_id(self, disciplina_id):
        for i in range(0, len(self.disciplinas)):
            if self.disciplinas[i].get_id() == disciplina_id:
                return self.disciplinas[i] 
        return None
