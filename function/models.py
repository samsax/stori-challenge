from peewee import *
import os
#rds settings
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
rds_host  = os.environ.get('rds_host','sql5.freemysqlhosting.net')
name = os.environ.get('db_username','sql5443524')
password = os.environ.get('db_password','GXJYwnIxQd')
db_name = os.environ.get('db_name','sql5443524')
logger.info(rds_host)
logger.info(name)
logger.info(db_name)
db = MySQLDatabase(db_name, user=name, password=password,
                         host=rds_host, port=3306)

class Account(Model):
    account_number = CharField()
    email = CharField()
    class Meta:
        database = db 


class Transaction(Model):
    owner = ForeignKeyField(Account, backref='transactions')
    create_date = DateField()
    amount = CharField()

    class Meta:
        database = db 