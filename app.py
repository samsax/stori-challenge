import sys
import csv
from models import db, Transaction, Person
import datetime

class Summary():
    def __init__(self,months_transacctions, balance, credit, debit):
        self.months_transacctions = months_transacctions
        self.balance = balance
        self.credit = credit
        self.debit = debit
        self.transaction = 0
    

def handler(event, context):
    print(db.connect())
    db.create_tables([Person, Transaction])
    input_file = csv.DictReader(open("txns.csv"))
    new_person = Person.create(name='Juan', email='juan@gmail.com')
    new_person.save()
    summary = summary_transacction(input_file, new_person)
    send_mail_summary(summary)
    
        

def summary_transacction(input_file, person):
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
    return Summary(months,balance,total_credit,total_debit)
    


def send_mail_summary(summary):
    pass


def average(lst):
    return round(sum(lst) / len(lst),2)
    

    

if __name__ == "__main__":
    handler(None,None)