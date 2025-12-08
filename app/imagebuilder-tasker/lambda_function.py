import json
import boto3
import time
from typing import Dict, Any

ssm = boto3.client('ssm')
codepipeline = boto3.client('codepipeline')
imagebuilder = boto3.client('imagebuilder')


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda function to orchestrate CodePipeline and EC2 Image Builder pipeline execution.
    
    Steps:
    1. Read SSM parameters
    2. Trigger CodePipeline: SimplePythonBuildService and wait for success
    3. Trigger EC2 Image Builder pipeline: imagebuilder-tester
    """
    try:
        # Step 1: Read SSM parameters
        parameters = read_ssm_parameters()
        print(f"Retrieved SSM parameters: {json.dumps(parameters, default=str)}")
        
        # Step 2: Trigger CodePipeline and wait for completion
        pipeline_name = 'SimplePythonBuildService'
        print(f"Starting CodePipeline: {pipeline_name}")
        
        pipeline_execution_id = trigger_codepipeline(pipeline_name)
        print(f"CodePipeline execution started: {pipeline_execution_id}")
        
        wait_for_pipeline_success(pipeline_name, pipeline_execution_id)
        print(f"CodePipeline {pipeline_name} completed successfully")
        
        # Step 3: Trigger EC2 Image Builder pipeline
        imagebuilder_pipeline_arn = parameters.get('imagebuilder_pipeline_arn', 
                                                    'arn:aws:imagebuilder:*:*:image-pipeline/imagebuilder-tester')
        print(f"Starting Image Builder pipeline: {imagebuilder_pipeline_arn}")
        
        image_build_version_arn = trigger_imagebuilder_pipeline(imagebuilder_pipeline_arn)
        print(f"Image Builder pipeline started: {image_build_version_arn}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Pipeline orchestration completed successfully',
                'codepipeline_execution_id': pipeline_execution_id,
                'imagebuilder_version_arn': image_build_version_arn
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Pipeline orchestration failed',
                'error': str(e)
            })
        }


def read_ssm_parameters() -> Dict[str, str]:
    """Read SSM parameters needed for pipeline execution."""
    parameter_names = [
        '/imagebuilder/pipeline/arn',
        '/codepipeline/name'
    ]
    
    parameters = {}
    for param_name in parameter_names:
        try:
            response = ssm.get_parameter(Name=param_name, WithDecryption=True)
            key = param_name.split('/')[-1]
            parameters[f"{param_name.split('/')[-2]}_{key}"] = response['Parameter']['Value']
        except ssm.exceptions.ParameterNotFound:
            print(f"Parameter {param_name} not found, using defaults")
        except Exception as e:
            print(f"Error reading parameter {param_name}: {str(e)}")
    
    return parameters


def trigger_codepipeline(pipeline_name: str) -> str:
    """Trigger CodePipeline execution and return execution ID."""
    response = codepipeline.start_pipeline_execution(name=pipeline_name)
    return response['pipelineExecutionId']


def wait_for_pipeline_success(pipeline_name: str, execution_id: str, timeout: int = 1800) -> None:
    """
    Wait for CodePipeline to complete successfully.
    
    Args:
        pipeline_name: Name of the pipeline
        execution_id: Pipeline execution ID
        timeout: Maximum wait time in seconds (default: 30 minutes)
    
    Raises:
        Exception: If pipeline fails or times out
    """
    start_time = time.time()
    
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Pipeline execution timed out after {timeout} seconds")
        
        response = codepipeline.get_pipeline_execution(
            pipelineName=pipeline_name,
            pipelineExecutionId=execution_id
        )
        
        status = response['pipelineExecution']['status']
        print(f"Pipeline status: {status}")
        
        if status == 'Succeeded':
            return
        elif status in ['Failed', 'Cancelled', 'Stopped']:
            raise Exception(f"Pipeline execution {status}: {execution_id}")
        
        time.sleep(30)


def trigger_imagebuilder_pipeline(pipeline_arn: str) -> str:
    """
    Trigger EC2 Image Builder pipeline execution.
    
    Args:
        pipeline_arn: ARN of the Image Builder pipeline
    
    Returns:
        Image build version ARN
    """
    response = imagebuilder.start_image_pipeline_execution(
        imagePipelineArn=pipeline_arn
    )
    return response['imageBuildVersionArn']
