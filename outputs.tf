output "cluster_name" {
  value = module.eks.cluster_name
}

output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}

output "ecr_user_service_url" {
  value = aws_ecr_repository.user_service.repository_url
}

output "ecr_product_service_url" {
  value = aws_ecr_repository.product_service.repository_url
}

output "jenkins_instance_profile" {
  value = aws_iam_instance_profile.jenkins.name
}