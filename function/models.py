from peewee import *
import os
#rds settings
rds_host  = os.environ.get('rds_host','sql5.freemysqlhosting.net')
name = os.environ.get('db_username','sql5443524')
password = os.environ.get('db_password','GXJYwnIxQd')
db_name = os.environ.get('db_name','sql5443524')
db = MySQLDatabase(name, user=db_name, password=password,
                         host=rds_host, port=3306)

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