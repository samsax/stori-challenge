import boto3

class S3File():
    def __init__(self,file,file_name):
        self.file = file
        self.file_name = file_name

class AwsServices():
    def __init__(self,event):
        self.event = event
    def get_s3_file(self):
        try:
            s3 = boto3.client('s3')
            file_identier = self.event["Records"][0]
            bucket_name = file_identier["s3"]["bucket"]["name"]
            file_name = file_identier["s3"]["object"]["key"]
            data = s3.get_object(Bucket=bucket_name, Key=file_name)
            file = data['Body'].read().decode("utf-8")
            return S3File(file,file_name)
        except Exception as exception:
            print("Error as: {}".format(exception))