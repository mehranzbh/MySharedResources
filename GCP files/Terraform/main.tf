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




resource "google_compute_instance" "terraformm" {
  project = "terraformtest-396803"
  name         = "test-instance-created-by-terraform"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      }
    }
  

  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }

 
  metadata_startup_script = "echo hi > /test.txt"

}
