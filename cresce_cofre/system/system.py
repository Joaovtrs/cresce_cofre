from .db_system import Acoes, database


class System:
    def __init__(self):
        self.caminho = None

    def abrir_db(self, caminho):
        if not database.is_closed():
            database.close()

        self.caminho = caminho
        database.init(self.caminho)

    def criar_db(self, caminho):
        self.abrir_db(caminho)
        database.create_tables([Acoes])
