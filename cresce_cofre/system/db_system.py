from logs import logger
from peewee import DoubleField, IntegerField, Model, SqliteDatabase, TextField

database = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = database


class Acoes(BaseModel):
    nome = TextField()
    key = TextField()
    quantidade = IntegerField()
    valor_medio = DoubleField()
    Valor_total = DoubleField()
