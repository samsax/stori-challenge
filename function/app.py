import csv
from account import get_or_create_account
from aws_services import AwsServices
from transaction import send_mail_summary, summary_transacction


def lambda_handler(event, _):
    awsServices = AwsServices(event)
    awsFile = awsServices.get_s3_file()
    new_person = get_or_create_account()
    input_file = csv.DictReader(awsFile.file)
    summary = summary_transacction(input_file, new_person)
    send_mail_summary(summary)


def main():
    input_file = csv.DictReader(open('./txns.csv'))
    new_person = get_or_create_account()
    summary = summary_transacction(input_file, new_person)
    send_mail_summary(summary)

if __name__ == '__main__':
    main()