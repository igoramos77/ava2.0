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

            Aula(10, 1, disciplinaDao.buscar_por_id(3), 'Aula 01', 'Desbravando o Adobe XD.', 'OH34SlpQE70'),
            Aula(11, 1, disciplinaDao.buscar_por_id(3), 'Aula 02', 'Adobe XD na prática.', 'OH34SlpQE70'),
            Aula(12, 1, disciplinaDao.buscar_por_id(3), 'Aula 03', 'comportamento do usuário.', 'OH34SlpQE70'),
            Aula(13, 1, disciplinaDao.buscar_por_id(3), 'Aula 04', 'Novas tendências.', 'OH34SlpQE70'),
            Aula(14, 1, disciplinaDao.buscar_por_id(3), 'Aula 05', 'Grid layout.', 'OH34SlpQE70'),
            Aula(15, 1, disciplinaDao.buscar_por_id(3), 'Aula 06', 'Flexbox.', 'OH34SlpQE70'),
            Aula(16, 1, disciplinaDao.buscar_por_id(3), 'Aula 07', 'Flexbox parte II.', 'OH34SlpQE70'),
            Aula(17, 1, disciplinaDao.buscar_por_id(3), 'Aula 08', 'Javascript UI.', 'OH34SlpQE70'),

            Aula(18, 1, disciplinaDao.buscar_por_id(2), 'Aula 01', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(19, 1, disciplinaDao.buscar_por_id(2), 'Aula 02', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(20, 1, disciplinaDao.buscar_por_id(2), 'Aula 03', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),

            Aula(21, 1, disciplinaDao.buscar_por_id(4), 'Aula 01', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(22, 1, disciplinaDao.buscar_por_id(4), 'Aula 02', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(23, 1, disciplinaDao.buscar_por_id(4), 'Aula 03', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(24, 1, disciplinaDao.buscar_por_id(4), 'Aula 04', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),
            Aula(25, 1, disciplinaDao.buscar_por_id(4), 'Aula 05', 'Lorem Ipsum is simply dummy.', 'OH34SlpQE70'),

            Aula(26, 1, disciplinaDao.buscar_por_id(6), 'Aula 01', 'SQL básico.', 'OH34SlpQE70'),
            Aula(27, 1, disciplinaDao.buscar_por_id(6), 'Aula 02', 'Mondelando um banco de dados.', 'OH34SlpQE70'),
        ]

        self._aula_list = []
        self._aula_list.append(Aula)        
        

    def listar_todas(self):
        return self.aulas

    def listar_todas_da_disciplina(self, disciplina_id):
        aulas_da_disciplina = []
        for i in range(0, len(self.aulas)):
            if self.aulas[i].get_disciplina().get_id() == disciplina_id:
                aulas_da_disciplina.append(self.aulas[i])
        return aulas_da_disciplina
        
        
    def buscar_por_id(self, id):
        for i in range(0, len(self.aulas)):
            if self.aulas[i].get_id() == id:
                return self.aulas[i] 
        return None
