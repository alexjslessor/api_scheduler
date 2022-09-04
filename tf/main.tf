terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}
variable "do_token" {}
# variable "domain_name" {}
# variable "private_key" {}
provider "digitalocean" {
  token = var.do_token
}
resource "digitalocean_app" "api_scheduler" {
  spec {
    name   = "api-sched"
    region = "tor"
    service {
      dockerfile_path = "Dockerfile"
      name               = "scheduler"
      instance_count     = 1
      instance_size_slug = "basic-xxs"
      http_port = 5000
      github {
        branch         = "master"
        deploy_on_push = true
        repo           = "alexjslessor/api_scheduler"
      }


    }
  }
}


# data "external" "droplet_name" {
#   program = ["python3", "${path.module}/external/name-generator.py"]
# }
# data "digitalocean_ssh_key" "ssh_key" {
#   name = "lenovo_dgo_sept13"
# }
# resource "digitalocean_droplet" "web" {
#   image  = "ubuntu-20-04-x64"
#   name   = data.external.droplet_name.result.name
#   region = "fra1"
#   size   = "s-1vcpu-1gb"
#   ssh_keys = [data.digitalocean_ssh_key.ssh_key.id]
#   connection {
#     # connection specifies how terraform should connect to target droplet
#     host        = self.ipv4_address
#     user        = "root"
#     type        = "ssh"
#     private_key = file(var.private_key)
#     timeout     = "2m"
#   }
#   provisioner "remote-exec" {
#     inline = [
#       "export PATH=$PATH:/usr/bin",
#       # Install Apache
#       "apt update",
#       "apt -y install apache2"
#     ]
#   }

# }

# resource "digitalocean_record" "www" {
#   domain = var.domain_name
#   type   = "A"
#   name   = "@"
#   value  = digitalocean_droplet.web.ipv4_address
# }

