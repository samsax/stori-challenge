import csv
from function.account import get_or_create_account
from function.aws_services import AwsServices
from function.transaction import send_mail_summary, summary_transacction
import os
import logging
from botocore.client import Config
import boto3
from io import StringIO
logger = logging.getLogger()
logger.setLevel(logging.INFO)
config = Config(connect_timeout=5, retries={'max_attempts': 0})
s3 = boto3.client('s3', config=config)
import pandas 
def lambda_handler(event, _):
    try:
        logger.info('## ENVIRONMENT VARIABLES')
        logger.info(os.environ)
        logger.info('## EVENT')
        logger.info(event)
        awsServices = AwsServices(event,s3)
        awsFile = awsServices.get_s3_file()
        logger.info(awsFile)
        new_person = get_or_create_account(awsFile.file_name)
        input_file = pandas.read_csv(awsFile.file).to_dict('records')
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
    except Exception as error:
        logger.info(error)


def main():
    file = open('./txns.csv')
    print(type(open('./txns.csv')))
    input_file =  pandas.read_csv(file).to_dict('records')
    print(input_file)
    new_person = get_or_create_account('txns')
    summary = summary_transacction(input_file, new_person)
    send_mail_summary(summary)

if __name__ == '__main__':
    main()