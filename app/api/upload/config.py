import boto3
from botocore.config import Config
from dotenv import dotenv_values
config = dotenv_values(".env")


bucket_name = config["BUCKET_NAME"]

my_config = Config(
            region_name = 'ap-south-1',
                signature_version = 'v4',
                    retries = {
                                'max_attempts': 10,
                                'mode': 'standard'
                              })

s3 = boto3.client('s3')
