terraform {
  backend "s3" {
    bucket = "golden-imagebuilder-tfstate"
    key    = "imagebuilder-tasker/terraform.tfstate"
    region = "us-east-1"
  }

  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.4"
    }
  }
}
