import csv
from function.account import get_or_create_account
from function.aws_services import AwsServices
from function.transaction import send_mail_summary, summary_transacction
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, _):
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)
    awsServices = AwsServices(event)
    awsFile = awsServices.get_s3_file()
    logger.info(awsFile)
    new_person = get_or_create_account()
    input_file = csv.DictReader(awsFile.file)
    logger.info(input_file)
    summary = summary_transacction(input_file, new_person)
    send_mail_summary(summary)
    return { 
        'message' : 'done',
        'summary' : {
            'balance' : summary.balance,
            'transaction' : summary.transaction,
        }
    }


def main():
    input_file = csv.DictReader(open('./txns.csv'))
    new_person = get_or_create_account()
    summary = summary_transacction(input_file, new_person)
    send_mail_summary(summary)

if __name__ == '__main__':
    main()