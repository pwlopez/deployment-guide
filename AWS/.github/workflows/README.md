This folder contains all the necesary components and a repo template for machine learning projects in AWS

TO DO:
- Organize folder structure
- Add Dockerfile for running custom model
- Add lambda handler for invoking Sagemaker endpoint
- Add script for deploying container to Sagemaker endpoint
    - add AWS credentials to Github Actions secrets for logging into boto3
    - extract registry tage and model name from build-tag-push step
- Add script for testing endpoint
- Add guide for setting permissions and roles in AWS
- Add requirements.txt
- Add infrastructure guide for serverless deployment
    - AWS Lambda
    - AWS API Gateway
- Add infrastructure guide for code deploy
    - AWS ECS