from src.summary import Summary
from src.models import db, Transaction
import datetime



def summary_transacction(input_file, person):
    if(not db.is_connection_usable):
        db.connect()
    months = {}
    total_credit = []
    total_debit = []
    for row in input_file:
        transaction = Transaction.create(amount=row['Transaction'], create_date=row['Date'], owner = person)
        transaction.save()
        create_date = datetime.datetime.strptime(row['Date'], '%m/%d').date()
        if create_date.month  in months:
            months[create_date.month] += 1   
        else: 
            months[create_date.month] = 1
        if(float(row['Transaction'])> 0):
            total_credit.append(float(row['Transaction']))
        else:
            total_debit.append(float(row['Transaction']))
    balance = sum(total_credit) + sum(total_debit)
    average_credit = average(total_credit)
    average_debit = average(total_debit)
    summary = Summary(months,balance,total_credit,total_debit)
    print(summary.balance)
    return summary
    


def send_mail_summary(summary):
    pass


def average(lst):
    return round(sum(lst) / len(lst),2)
