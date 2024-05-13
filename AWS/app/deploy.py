import os
import boto3
from datetime import datetime

# All of these are pulled form repo enviornemnt secrets
REGION = os.environ["AWS_REGION"]
ACCESS_KEY = os.environ["AWS_ACCESS_KEY_ID"]
SECRET_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
ROLE = ""

session = boto3.Session(
    aws_secret_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

sm_client = session.client("sagemaker")

model_name = ""
model_path = f"s3://PATH/TO/MODEL/{model_name}.tar.gz"
image_name = f"{ACCESS_KEY}.dkr.ecr.{REGION}.amazonaws.com/[IMAGE TAG]:latest"

primary_container = {
    "Image": image_name,
    "ModelDataUrl": model_path
}

create_model_response = sm_client.create_model(
    ModelName=model_name,
    ExecutionRoleArn=ROLE,
    PrimaryContainer=primary_container)