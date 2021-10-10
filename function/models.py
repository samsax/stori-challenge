from peewee import *

db = MySQLDatabase('database-1', user='admin', password='challenge',
                         host='database-1.cjyf1rwy9oid.us-east-2.rds.amazonaws.com', port=3306)

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