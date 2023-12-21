from peewee import Model, SqliteDatabase, TextField, DoubleField, IntegerField
from loguru import logger

database = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = database


class Acoes(BaseModel):
    logger.info('Inicializando classe Acoes')

    nome = TextField()
    key = TextField()
    quantidade = IntegerField()
    valor_medio = DoubleField()
    Valor_total = DoubleField()
