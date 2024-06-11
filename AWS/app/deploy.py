import os
import boto3
from datetime import datetime

# https://towardsdatascience.com/deploy-a-custom-ml-model-as-a-sagemaker-endpoint-6d2540226428

REGION = os.environ["AWS_REGION"]
ACCESS_KEY = os.environ["AWS_ACCESS_KEY_ID"]
SECRET_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
ROLE = ""
ECR_REGISTRY = os.environ["ECR_REGISTRY"]
MODEL_NAME = os.environ["MODEL_NAME"]
MODEL_PATH = os.environ["MODEL_PATH"]

session = boto3.Session(
    aws_secret_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

sm_client = session.client("sagemaker")

primary_container = {
    "Image": ECR_REGISTRY,
    "ModelDataUrl": MODEL_PATH
}

create_model_response = sm_client.create_model(
    ModelName=MODEL_NAME,
    ExecutionRoleArn=ROLE,
    PrimaryContainer=primary_container)

endpoint_config_name = f"{MODEL_NAME}-config-{datetime.now()}"

sm_client.create_endpoint_config(
    EndpointConfigName=endpoint_config_name,
    ProductionVariants=[{
        "InstanceType": "ml.g5.xlarge",
        "InitialVariantWeight": 1,
        "InitialInstanceCount": 1,
        "ModelName": MODEL_NAME,
        "VariantName": "AllTraffic"}])

endpoint_name = f"{MODEL_NAME}-endpoint-{datetime.now()}"

sm_client.create_endpoint(
    EndpointName=endpoint_name,
    EndpointConfigName=endpoint_config_name)

# Use this to add the endpoint name to github action env so that we may
# have access to it for testing
github_env = os.getenv("GITHUB_ENV")
with open(github_env, "a") as myfile:
    myfile.write(f"ENDPOINT_NAME={endpoint_name}")