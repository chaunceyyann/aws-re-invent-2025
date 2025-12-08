# ImageBuilder Tasker Terraform

Terraform configuration for deploying the ImageBuilder Tasker Lambda function.

## Backend

Uses S3 backend: `arn:aws:s3:::golden-imagebuilder-tfstate`

## Resources Created

- Lambda function with Python 3.11 runtime
- IAM role and policy with permissions for SSM, CodePipeline, and Image Builder
- CloudWatch Log Group with 7-day retention

## Usage

```bash
# Initialize Terraform
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy resources
terraform destroy
```

## Variables

| Name | Description | Default |
|------|-------------|---------|
| aws_region | AWS region | us-east-1 |
| environment | Environment name | dev |
| lambda_function_name | Lambda function name | imagebuilder-tasker |
| lambda_timeout | Timeout in seconds | 900 |
| lambda_memory_size | Memory in MB | 256 |
| codepipeline_name | CodePipeline name | SimplePythonBuildService |
| imagebuilder_pipeline_name | Image Builder pipeline name | imagebuilder-tester |

## Outputs

- `lambda_function_arn` - Lambda function ARN
- `lambda_function_name` - Lambda function name
- `lambda_role_arn` - IAM role ARN
- `lambda_log_group` - CloudWatch Log Group name
