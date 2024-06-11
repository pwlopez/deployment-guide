import os
import json
import boto3

ACCESS_KEY = os.environ["AWS_ACCESS_KEY_ID"]
SECRET_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
ENDPOINT_NAME = os.environ["ENDPOINT_NAME"]

session = boto3.Session(
    aws_secret_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

sm_client = session.client("sagemaker")

payload = json.loads("/test_file.json")

response = sm_client.invoke_endpoint(
    EndpointName=ENDPOINT_NAME,
    ContentType="image/x-image",
    Body=payload
)

response = json.loads(response["Body"].read().decode())