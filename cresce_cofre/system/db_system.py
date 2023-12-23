from logs import logger
from peewee import (BooleanField, DateField, DoubleField, ForeignKeyField,
                    IntegerField, Model, SqliteDatabase, TextField)

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


class Transacoes(BaseModel):
    data = DateField()
    acao = ForeignKeyField(Acoes, backref='transacoes')
    quantidade = IntegerField()
    Valor = DoubleField()
    is_compra = BooleanField()
