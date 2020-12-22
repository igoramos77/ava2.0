class Professor:

    def __init__(self, id, nome, email, avatar, linkdedin):
        self._id = id
        self._nome = nome
        self._email = email
        self._avatar = avatar
        self._linkdedin = linkdedin
    
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email
    
    def get_avatar(self):
        return self._avatar
    
    def get_linkedin(self):
        return self._linkdedin
        