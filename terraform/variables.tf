variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "imagebuilder-tasker"
}

variable "lambda_timeout" {
  description = "Lambda function timeout in seconds"
  type        = number
  default     = 900
}

variable "lambda_memory_size" {
  description = "Lambda function memory size in MB"
  type        = number
  default     = 256
}

variable "codepipeline_name" {
  description = "Name of the CodePipeline to trigger"
  type        = string
  default     = "SimplePythonBuildService"
}

variable "imagebuilder_pipeline_name" {
  description = "Name of the Image Builder pipeline"
  type        = string
  default     = "imagebuilder-tester"
}
