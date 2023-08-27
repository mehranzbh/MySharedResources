
resource "google_compute_network" "mynetwork" {
  name = var.network_name
  # RESOURCE properties go here
  auto_create_subnetworks = "true"
}
