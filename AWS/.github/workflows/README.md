This folder contains all the necesary components and a repo template for machine learning projects in AWS. There are 2 deployment methods
covered in this repo for AWS:

    1. Train a supported model with Sagemaker notebooks and deploy as an Sagemaker Endpoint. Use AWS Lambda and API Gateway to make is accessible.
    1. Upload and deploy a pre-trained custom model as a Sagemaker Endpoint. Use AWS Lambda and API Gateway to make is accessible.
    2. Deploy a custom pre-trained and self-hosted model with API on EC2

There are a few other things that can be done including building a fully custom container for training and serving a model
not already supported by Sagemaker.

TO DO:
- Add script for deploying container to Sagemaker endpoint
    - add AWS credentials to Github Actions secrets for logging into boto3
    - extract registry and model name from build-tag-push step
- Add script for testing endpoint
- Add guide for setting permissions and roles in AWS
- Add requirements.txt
- Add infrastructure guide for serverless deployment
    - AWS Lambda
    - AWS API Gateway
- Add infrastructure guide for code deploy
    - AWS ECS
- Add logging tools
    - raw inputs
    - transformed inputs
    - model outputs
    - 


* NOTE: add assertions for function parameter types to ensure the function is getting
only EXACTLY what it requires or crash