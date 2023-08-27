provider "google" {}

##this module will pass the network_name to the server_VM1 by defining this variable in the network/outputs.tf file
module "server_VM1_network" {
    source = "./network"
    network_name = "mytestnetwork"
}


## this module will take the server name from ./network/outputs.tf file
module "server_VM1" {
    source = "./server"
    instance_name = "vm1-defined-in-tfvars"
    instance_zone = "us-central1-a"
    network_name = module.server_VM1_network.network_name
}

