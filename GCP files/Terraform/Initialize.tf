#the file name should be changed to main.tf after plugins has been installed (provider plugins - GCP plugins), then the terraform plan command with the main.tf revised file (which includes further configuration) should be run.

terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.79.0"
    }
  }
}

provider "google" {
  project = "terraformtest-396803"

}
