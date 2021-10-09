from src.models import db, Account, Transaction 

def get_or_create_account():
    if(not db.is_connection_usable):
        db.connect()
    db.create_tables([Account])
    new_account = Account.create(name='Juan', email='juan@gmail.com')
    new_account.save()
    return new_account