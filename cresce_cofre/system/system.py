from loguru import logger

from .db_system import Acoes, Transacoes, database


class System:
    def __init__(self):
        logger.log('CLASS', 'Criando classe "System"')

        self.caminho = None
        self.is_open = False

    def abrir_db(self, caminho):
        logger.log('METHOD', 'Chamando função "System.abrir_db"')

        if not database.is_closed():
            logger.debug('Banco de dados fechado')
            database.close()

        self.caminho = caminho
        database.init(self.caminho)
        self.is_open = True

    def criar_db(self, caminho):
        logger.log('METHOD', 'Chamando função "System.criar_db"')

        self.abrir_db(caminho)
        database.create_tables([Acoes, Transacoes])

    @staticmethod
    def get_acoes():
        logger.log('METHOD', 'Chamando função "System.get_acao"')

        response = Acoes.select()
        result = [item for item in response.dicts()]

        return result

    @staticmethod
    def add_acao(_nome, _key, _quantidade, _valor_medio, _valor_total):
        logger.log('METHOD', 'Chamando função "System.add_acao"')

        Acoes.create(
            nome=_nome,
            key=_key,
            quantidade=_quantidade,
            valor_medio=_valor_medio,
            valor_total=_valor_total
        )

    @staticmethod
    def excluir_acao(_id):
        logger.log('METHOD', 'Chamando função "System.excluir_acao"')

        Acoes.delete().where(Acoes.id == _id).execute()

    @staticmethod
    def modificar_acao(_id, campo, valor):
        logger.log('METHOD', 'Chamando função "System.modificar_acao"')

        if campo == 'nome':
            response = Acoes.select().where(Acoes.id == _id).get()
            response.nome = valor
            response.save()
        if campo == 'key':
            response = Acoes.select().where(Acoes.id == _id).get()
            response.key = valor
            response.save()


sistema = System()
