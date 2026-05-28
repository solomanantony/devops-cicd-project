variable "aws_region" {
  default = "ap-south-2"
}

variable "project_name" {
  default = "devops-cicd"
}

variable "environment" {
  default = "dev"
}

variable "eks_node_instance_type" {
  default = "t3.medium"
}

variable "eks_node_desired" {
  default = 2
}

variable "eks_node_min" {
  default = 1
}

variable "eks_node_max" {
  default = 3
}