# ImageBuilder Tasker Lambda

Lambda function that orchestrates AWS CodePipeline and EC2 Image Builder pipeline execution.

## Functionality

1. **Read SSM Parameters**: Retrieves configuration from AWS Systems Manager Parameter Store
2. **Trigger CodePipeline**: Starts `SimplePythonBuildService` pipeline and waits for successful completion
3. **Trigger Image Builder**: Starts `imagebuilder-tester` EC2 Image Builder pipeline

## SSM Parameters

The function reads the following SSM parameters (optional):
- `/imagebuilder/pipeline/arn` - Image Builder pipeline ARN
- `/codepipeline/name` - CodePipeline name

## IAM Permissions Required

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:GetParameter"
      ],
      "Resource": "arn:aws:ssm:*:*:parameter/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "codepipeline:StartPipelineExecution",
        "codepipeline:GetPipelineExecution"
      ],
      "Resource": "arn:aws:codepipeline:*:*:SimplePythonBuildService"
    },
    {
      "Effect": "Allow",
      "Action": [
        "imagebuilder:StartImagePipelineExecution"
      ],
      "Resource": "arn:aws:imagebuilder:*:*:image-pipeline/imagebuilder-tester"
    }
  ]
}
```

## Configuration

- **Timeout**: Recommended 15 minutes (900 seconds)
- **Memory**: 256 MB
- **Runtime**: Python 3.11

## Deployment

```bash
cd app/imagebuilder-tasker
pip install -r requirements.txt -t .
zip -r function.zip .
aws lambda update-function-code --function-name imagebuilder-tasker --zip-file fileb://function.zip
```
