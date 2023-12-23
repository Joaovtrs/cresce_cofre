from logs import logger

from .db_system import Acoes, Transacoes, database


class System:
    @logger.class_init
    def __init__(self):
        self.caminho = None

    @logger.class_method_init
    def abrir_db(self, caminho):
        if not database.is_closed():
            database.close()

        self.caminho = caminho
        database.init(self.caminho)

    @logger.class_method_init
    def criar_db(self, caminho):
        self.abrir_db(caminho)
        database.create_tables([Acoes, Transacoes])


sistema = System()
