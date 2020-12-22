class Periodo:

    def __init__(self, id, nome, disciplina_lista):
        self._id = id
        self._nome = nome
        self._disciplina_lista = disciplina_lista
    
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_disciplina_lista(self):
        return self._disciplina_lista