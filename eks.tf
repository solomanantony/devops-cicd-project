module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "${var.project_name}-cluster"
  cluster_version = "1.29"

  vpc_id                         = module.vpc.vpc_id
  subnet_ids                     = module.vpc.private_subnets
  cluster_endpoint_public_access = true

  eks_managed_node_groups = {
    main = {
      instance_types = [var.eks_node_instance_type]
      min_size       = var.eks_node_min
      max_size       = var.eks_node_max
      desired_size   = var.eks_node_desired

      labels = {
        Environment = var.environment
      }
    }
  }

  # Enable IRSA
  enable_irsa = true

  tags = {
    Project     = var.project_name
    Environment = var.environment
  }
}