# AWS Shutdown Python Script
Get temporary sts credentials and shut down running instances on aws

## Prequistes: 

To run the script I provided in the previous responses, you need to ensure that your environment meets the following requirements:

1. **Python Installed**: You need to have Python installed on your system. The script is written in Python.

2. **AWS CLI Configuration**: You should have AWS CLI (Command Line Interface) configured with appropriate credentials and default region. You can configure it by running `aws configure` and providing your AWS access key, secret key, default region, and output format.

3. **Boto3 Installed**: Install the `boto3` library, which is the AWS SDK for Python. You can install it using pip:

   ```
   pip install boto3
   ```

4. **IAM Role and Permissions**: Ensure that you have an IAM role set up in your AWS account with the necessary permissions (e.g., EC2 administration) and trust relationships for your AWS EC2 instances to assume this role.

5. **AWS Environment Variables (Optional)**: You can set environment variables for `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, and `AWS_DEFAULT_REGION` if you prefer not to use the AWS CLI configuration. These environment variables will override the CLI configuration if set.

6. **AWS CLI Tools**: If you want to run the AWS CLI commands within the script (e.g., `aws configure` or `aws sts assume-role`), you need to have the AWS CLI tools installed.

Make sure to replace `"arn:aws:iam::YOUR_ACCOUNT_ID:role/EC2AdminRole"` with the actual ARN of your IAM role.
