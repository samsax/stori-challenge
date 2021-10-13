from function.models import db, Account 
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_or_create_account(file_name):
    try:
        logger.info('## GETTING OR CREATING AN ACCOUNT')
        if(not db.is_connection_usable):
            logger.info('## request DB Connection')
            db.connect()
            logger.info('## DB Connect')
        db.create_tables([Account])
        account = Account.select().where(Account.account_number==file_name)
        if(account):
            return account
        else:
            new_account = Account.create(account_number=file_name, email='samuelsaxofon@gmail.com')
            new_account.save()
            return new_account
    except Exception as error:
         logger.info("Error on create account {}".format(error)) 