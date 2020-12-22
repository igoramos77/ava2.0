class Disciplina:

    def __init__(self, id, nome, professor, periodo, dia_semana, horario):
        self._id = id
        self._nome = nome
        self._professor = professor
        self._periodo = periodo
        self._dia_semana = dia_semana
        self._horario = horario
    
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome
    
    def get_periodo(self):
        return self._periodo
    
    def get_dia_semana(self):
        return self._dia_semana
    
    def get_horario(self):
        return self._horario
    
    def get_professor(self):
        return self._professor