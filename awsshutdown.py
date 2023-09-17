import os
import boto3
import logging

# Set up simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Retrieve AWS credentials and configuration from environment variables
access_key = os.environ.get("AWS_ACCESS_KEY_ID")
secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
session_token = os.environ.get("AWS_SESSION_TOKEN")
aws_region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")

# Create an STS client
sts = boto3.client(
    "sts",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=aws_region,
    aws_session_token=session_token,
)

# Get the STS identity
sts_identity = sts.get_caller_identity()

# Assume the EC2 admin role to get temporary credentials
sts_response = sts.assume_role(
    RoleArn="arn:aws:iam::YOUR_ACCOUNT_ID:role/EC2AdminRole",  # Replace with your role ARN
    RoleSessionName="EC2AdminSession",
)

# Extract temporary credentials
temporary_credentials = sts_response["Credentials"]

# Create an EC2 client using temporary credentials
ec2 = boto3.client(
    "ec2",
    aws_access_key_id=temporary_credentials["AccessKeyId"],
    aws_secret_access_key=temporary_credentials["SecretAccessKey"],
    aws_session_token=temporary_credentials["SessionToken"],
    region_name=aws_region,
)

# Describe EC2 instances
instances = ec2.describe_instances()

# Check if there are running instances
if instances["Reservations"]:
    instances = instances["Reservations"]
    print(f"We found {len(instances)} reservations in the account!")

    # Iterate through reservations to show all running instances and their identities
    for reservation in instances:
        for instance in reservation["Instances"]:
            print(f'Instance ID: {instance["InstanceId"]}')
            print(f'Instance State: {instance["State"]["Name"]}')
            print(f'STS Identity: {sts_identity}')
            # Add more instance details as needed
else:
    print("No running instances found in the account.")
