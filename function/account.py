from function.models import db, Account 
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


logger = logging.getLogger()
logger.setLevel(logging.INFO)
def get_or_create_account():
    if(not db.is_connection_usable):
        logger.info('## request DB Connection')
        db.connect()
        logger.info('## DB Connect')
    db.create_tables([Account])
    new_account = Account.create(name='Juan', email='juan@gmail.com')
    new_account.save()
    return new_account