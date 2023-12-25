from loguru import logger

from .db_system import Acoes, Transacoes, database


class System:
    def __init__(self):
        self.caminho = None
        self.is_open = False

    def abrir_db(self, caminho):
        if not database.is_closed():
            database.close()

        self.caminho = caminho
        database.init(self.caminho)
        self.is_open = True

    def criar_db(self, caminho):
        self.abrir_db(caminho)
        database.create_tables([Acoes, Transacoes])

    @staticmethod
    def add_acao(_nome, _key, _quantidade, _valor_medio, _valor_total):
        Acoes.create(
            nome=_nome,
            key=_key,
            quantidade=_quantidade,
            valor_medio=_valor_medio,
            valor_total=_valor_total
        )

    @staticmethod
    def get_acoes():
        response = Acoes.select()
        result = []

        for item in response.dicts():
            result.append(item)

        return result


sistema = System()
