
## this module will take the server name from ./network/outputs.tf file
module "server_VM1" {
    source = ./server
    network_name = module.mynetwork.network_name
}

##this module will pass the network_name to the server_VM1 by defining this variable in the network/outputs.tf file
module "server_VM1_network" {
    source = ./network
}