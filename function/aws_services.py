import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
BUCKET = db_name = os.environ.get('db_name','csvlambdabucket')


class S3File():
    def __init__(self,file,file_name):
        self.file = file
        self.file_name = file_name

class AwsServices():
    def __init__(self,event,s3):
        self.event = event
        self.s3 = s3
    def get_s3_file(self):
        try:    
            file_identier = self.event["Records"][0]
            bucket_name = file_identier["s3"]["bucket"]["name"]
            file_name = file_identier["s3"]["object"]["key"]
            data = self.s3.get_object(Bucket=bucket_name, Key=file_name)
            file = data['Body'].read().decode("utf-8")
            logger.info(file)
            logger.info(file_name)
            return S3File(file,file_name)
        except Exception as exception:
            logger.info("Error when get S3 file: {}".format(exception))