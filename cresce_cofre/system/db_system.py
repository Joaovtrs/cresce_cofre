from peewee import Model, SqliteDatabase, TextField

database = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = database


class Acoes(BaseModel):
    nome = TextField()
    key = TextField()
