
resource "google_compute_network" "my_network" {
  name = var.network_name
  # RESOURCE properties go here
  auto_create_subnetworks = "true"
}


##copy this to reference in the root main.tf file for instance network_name: module.mynetwork.network_name
