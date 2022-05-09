import boto3
from botocore.exceptions import ClientError

from .config import s3, bucket_name
import logging

log = logging.getLogger("my-logger")


def generate_presigned_url(s3_client, client_method, method_parameters, expires_in):
    """
    Generating a presigned Amazon S3 URL that can be used to perform an action.
    """
    try:
        url = s3_client.generate_presigned_url(
            ClientMethod=client_method,
            Params=method_parameters,
            ExpiresIn=expires_in
        )
        log.info("Got presigned URL")
    except ClientError:
        log.info(
            f"Couldn't get a presigned URL for client method {client_method}")
        raise
    return url


def upload_file(obj):
    client_action = 'put_object'
    file_path = obj.file_name
    url = generate_presigned_url(
        s3, client_action, {'Bucket': bucket_name, 'Key': file_path}, 3600)
    return {"presigned_url": url, "filename": obj.file_name}
