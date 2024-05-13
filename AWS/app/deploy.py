import os
import boto3

session = boto3.Session(
    aws_secret_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
)

sm_client = session.client("sagemaker")