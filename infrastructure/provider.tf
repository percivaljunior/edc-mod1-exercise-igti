provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket = "terraform-state-igti-percival"
    key = "state/igti/edc/mod1/terraform.tfstate"
    region = "sa-east-1"
  }
}