from logging import exception
from function.summary import Summary
from function.models import db, Transaction
from datetime import datetime 
from function.email_sender import SendMail
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def summary_transacction(input_file, person):
    if(not db.is_connection_usable):
        db.connect()
    db.create_tables([Transaction])
    months = {}
    total_credit = []
    total_debit = []
    for row in input_file:
        try:
            logger.info(row)
            create_date = datetime.strptime(row['Date'], '%m/%d').date()
            create_date = create_date.replace(year= datetime.now().year)
            logger.info(str(create_date))
            transaction = Transaction.create(amount=row['Transaction'], create_date=str(create_date), owner = person)
            logger.info(transaction)
            transaction.save()
            if create_date.month  in months:
                months[create_date.month] += 1   
            else: 
                months[create_date.month] = 1
            if(float(row['Transaction'])> 0):
                total_credit.append(float(row['Transaction']))
            else:
                total_debit.append(float(row['Transaction']))
        except Exception as error:
            print(error)
            logger.info("Error when proccesing file: {}".format(error))
    balance = sum(total_credit) + sum(total_debit)
    summary = Summary(months,balance,total_credit,total_debit)

    return summary
    


def send_mail_summary(summary):
    sendMail = SendMail(summary)
    sendMail.send()


