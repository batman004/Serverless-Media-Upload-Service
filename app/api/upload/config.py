import boto3
from botocore.config import Config
from dotenv import dotenv_values
import os
config = dotenv_values(".env")

os.environ['AWS_ACCESS_KEY_ID'] = config['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = config['AWS_SECRET_ACCESS_KEY']

bucket_name = "backend-lambda-bucket"

my_config = Config(
            region_name = 'ap-south-1',
                signature_version = 'v4',
                    retries = {
                                'max_attempts': 10,
                                'mode': 'standard'
                              })
s3 = boto3.client('s3')


