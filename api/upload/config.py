import boto3
import os
from botocore.config import Config
from dotenv import dotenv_values

config = dotenv_values(".env")

bucket_name = "backend-lambda-bucket"

os.environ['AWS_ACCESS_KEY_ID'] = config['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = config['AWS_SECRET_ACCESS_KEY']
os.environ['AWS_DEFAULT_REGION'] = config['AWS_DEFAULT_REGION']

my_config = Config(
    region_name='ap-south-1',
    signature_version='v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    })
s3 = boto3.client('s3')
