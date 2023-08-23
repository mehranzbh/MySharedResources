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
