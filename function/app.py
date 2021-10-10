import csv
from account import get_or_create_account
from transaction import send_mail_summary, summary_transacction


def lambda_handler(event, context):
    new_person = get_or_create_account()
    input_file = csv.DictReader(open("txns.csv"))
    summary = summary_transacction(input_file, new_person)
    send_mail_summary(summary)
