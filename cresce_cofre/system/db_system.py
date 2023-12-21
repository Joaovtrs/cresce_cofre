from peewee import Model, SqliteDatabase, TextField, DoubleField, IntegerField

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
