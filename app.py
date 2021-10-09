import sys
import csv
from src.account import get_or_create_account
from src.transaction import send_mail_summary, summary_transacction
    
def handler(event, context):
    new_person = get_or_create_account()
    input_file = csv.DictReader(open("txns.csv"))
    summary = summary_transacction(input_file, new_person)
    send_mail_summary(summary)

if __name__ == "__main__":
    handler(None,None)