import boto3
import os
from botocore.config import Config
from dotenv import dotenv_values

config = dotenv_values(".env")

bucket_name = "backend-lambda-bucket"

os.environ.get('AWS_ACCESS_KEY_ID')
os.environ.get('AWS_SECRET_ACCESS_KEY')
os.environ.get('AWS_DEFAULT_REGION')

my_config = Config(
    region_name='ap-south-1',
    signature_version='v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    })
s3 = boto3.client('s3')
