from .db_system import Acoes, database
from loguru import logger


class System:
    def __init__(self):
        logger.info('Inicializando classe System')

        self.caminho = None

    def abrir_db(self, caminho):
        logger.info('Chamada de função "abrir_db" no System')

        if not database.is_closed():
            database.close()

        self.caminho = caminho
        database.init(self.caminho)

    def criar_db(self, caminho):
        logger.info('Chamada de função "criar_db" no System')

        self.abrir_db(caminho)
        database.create_tables([Acoes])


sistema = System()
