from loguru import logger
from peewee import (BooleanField, DateField, DoubleField, ForeignKeyField,
                    IntegerField, Model, SqliteDatabase, TextField)

database = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = database


class Acoes(BaseModel):
    nome = TextField()
    key = TextField()
    quantidade = IntegerField(null=True, default=0)
    valor_medio = DoubleField(null=True, default=0.0)
    valor_total = DoubleField(null=True, default=0.0)


class Transacoes(BaseModel):
    data = DateField()
    acao = ForeignKeyField(Acoes, backref='transacoes')
    quantidade = IntegerField()
    Valor = DoubleField()
    is_compra = BooleanField()
