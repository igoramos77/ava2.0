from application.model.entity.disciplina import Disciplina
from application.model.entity.aula import Aula
from application.model.dao.disciplina_dao import DisciplinaDAO

class AulaDAO():
    def __init__(self):
        disciplinaDao = DisciplinaDAO()
        self.aulas = [
            #(self, id, modulo_id, disciplina_id, nome, descricao, video_url)
            Aula(1, 1, disciplinaDao.buscar_por_id(1), 'Aula 01', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(2, 1, disciplinaDao.buscar_por_id(1), 'Aula 02', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(3, 1, disciplinaDao.buscar_por_id(1), 'Aula 03', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(4, 1, disciplinaDao.buscar_por_id(1), 'Aula 04', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(5, 1, disciplinaDao.buscar_por_id(1), 'Aula 05', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(6, 1, disciplinaDao.buscar_por_id(1), 'Aula 06', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(7, 1, disciplinaDao.buscar_por_id(1), 'Aula 07', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(8, 1, disciplinaDao.buscar_por_id(1), 'Aula 08', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(9, 1, disciplinaDao.buscar_por_id(1), 'Aula 09', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
        ]

        self._aula_list = []
        self._aula_list.append(Aula)        
        

    def listar_todas(self):
        return self.aulas

    def listar_todas_da_disciplina(self, disciplina_id):
        for i in range(0, len(self.aulas)):
            if self.aulas[i].get_disciplina_id() == disciplina_id:
                return self.aulas[i]
        return None
        
        
    def buscar_por_id(self, id):
        for i in range(0, len(self.aulas)):
            if self.aulas[i].get_id() == id:
                return self.aulas[i] 
        return None
