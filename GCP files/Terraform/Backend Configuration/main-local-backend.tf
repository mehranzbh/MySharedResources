provider "google" {
  project = "qwiklabs-gcp-03-b9e9c00bd8b0"
  region  = "us-central-1"
}
resource "google_storage_bucket" "test-bucket-for-state" {
  name        = "qwiklabs-gcp-03-b9e9c00bd8b0"
  location    = "US"
  uniform_bucket_level_access = true
  force_destroy = true
}
terraform {
  backend "local" {
    path = "terraform/state/terraform.tfstate"
  }
}
