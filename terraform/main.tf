provider "digitalocean" {
  token = var.do_token
}

resource "digitalocean_droplet" "gpu_vm" {
  image  = "ubuntu-22-04-x64"
  name   = "gpu-server"
  region = "nyc3"
  size   = "g-2vcpu-8gb"
  ssh_keys = [var.ssh_fingerprint]
}
