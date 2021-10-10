from peewee import *

db = MySQLDatabase('sql5443524', user='sql5443524', password='GXJYwnIxQd',
                         host='sql5.freemysqlhosting.net', port=3306)

class Account(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db # This model uses the "stori.db" database.


class Transaction(Model):
    owner = ForeignKeyField(Account, backref='transactions')
    create_date = DateField()
    amount = CharField()

    class Meta:
        database = db # this model uses the "stori.db" database