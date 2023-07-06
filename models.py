from peewee import *

# database connection
db = SqliteDatabase("shopyoo.sqlite3")

class Inventory(Model):
    name = CharField(unique=True)
    price = IntegerField()
    quantity = IntegerField()

    class Meta:
        database = db

def create_tables():
    # create tables in sqllite db
    with db:
        db.create_tables([Inventory])

