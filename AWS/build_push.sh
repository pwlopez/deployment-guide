#!/bin/bash

export AWS_PROFILE=analytics-dev

# Set vars
REGION="us-west-2"
IMAGE="sync-lambda"
REPOSITORY="sync-lambda"

# Get account id
ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)

# Login
aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

# Check if repo exists in ECR, if not create repo
aws ecr describe-repositories --repository-names ${REPOSITORY} || aws ecr create-repository --repository-name ${REPOSITORY}

# Build docker image
docker build -t ${IMAGE} .

# tag docker image
docker tag ${IMAGE} ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPOSITORY}:latest

# Push docker image to ECR
docker push ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPOSITORY}:latest

echo "Complete!"