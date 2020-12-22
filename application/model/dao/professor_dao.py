from application.model.entity.professor import Professor
from datetime import datetime

class ProfessorDAO:
    def __init__(self):
        self.professores = [
            Professor(1, 'Marco Antônio', 'marcoantonio@gmail.com', None or 'avatar-prof.svg', 'https://br.linkedin.com/in/marco-antônio-araújo-020bab3b'),
            Professor(2, 'Tássio Auad', 'auadtassio@gmail.com', 'tassio.svg' or 'avatar-prof.svg', 'https://www.linkedin.com/in/tassioauad/'),
            Professor(3, 'Anrafel Fernandes', 'anrafel@gmail.com', None or 'avatar-prof.svg', 'https://www.linkedin.com/in/anrafael/'),
            Professor(4, 'Maria Fernanda', 'maria@gmail.com', None or 'avatar-prof.svg', 'https://www.linkedin.com/in/maria/'),
            Professor(5, 'Claudenir', 'claudenir@gmail.com', None or 'avatar-prof.svg', 'https://www.linkedin.com/in/claudenir/'),
            Professor(6, 'Cléber Paschoal', 'cleber@gmail.com', None or 'avatar-prof.svg', 'https://www.linkedin.com/in/cleber/'),
        ]

        self._professor_list = []
        self._professor_list.append(Professor)

    def buscar_por_id(self, id):
        for i in range(0, len(self.professores)):
            if self.professores[i].get_id() == id:
                return self.professores[i] 
        return None


        


    