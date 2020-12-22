class Aula:

    def __init__(self, id, modulo_id, disciplina, nome, descricao, video_url):
        self._id = id
        self._modulo_id = modulo_id
        self._disciplina = disciplina
        self._nome = nome
        self._descricao = descricao
        self._video_url = video_url
    
    def get_id(self):
        return self._id
    
    def get_modulo_id(self):
        return self._modulo_id
    
    def get_disciplina(self):
        return self._disciplina

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao

    def get_video_url(self):
        return self._video_url

