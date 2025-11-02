output "app_public_ip" {
  value = digitalocean_droplet.app.ipv4_address
}
