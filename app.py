from function.email_sender import SendMail
from function.transaction import Transactions
from function.account import get_or_create_account
from function.aws_services import AwsServices
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
        input_file = pandas.read_csv(StringIO(awsFile.file)).to_dict('records')
        logger.info(input_file)
        transacctions = Transactions()
        summary = transacctions.summary_transacction(input_file, new_person)
        sendMail = SendMail(summary)
        sendMail.send()
        return { 
            'message' : 'done',
            'summary' : {
                'balance' : summary.balance,
            }
        }
    except Exception as error:
        logger.info(error)


def main():
    file = open('./txns.csv')
    input_file =  pandas.read_csv(file).to_dict('records')
    new_person = get_or_create_account('txns.csv')
    transacctions = Transactions()
    summary = transacctions.summary_transacction(input_file, new_person)
    sendMail = SendMail(summary)
    sendMail.send()

if __name__ == '__main__':
    main()