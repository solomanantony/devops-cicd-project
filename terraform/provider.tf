terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }

  # S3 backend 
  backend "s3" {
    bucket         = "devops-project-tfstate-soloman"
    key            = "eks/terraform.tfstate"
    region         = "ap-south-2"
    dynamodb_table = "terraform-lock-soloman"
    encrypt        = true
  }
}

provider "aws" {
  region = var.aws_region
}