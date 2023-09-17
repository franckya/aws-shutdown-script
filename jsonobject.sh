# AWS CLI command to assume an IAM role using STS
aws sts assume-role \
    --role-arn arn:aws:iam::typeyouriamidhere:role/typeyouriamrolehere \ # Replace with your actual role ARN
    --role-session-name $(echo $RANDOM | base64 | head -c 20; echo) \ # Generate a random session name
    --profile cloud_user # Specify an AWS CLI profile
