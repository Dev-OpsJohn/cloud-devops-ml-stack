# Automated Cloud DevOps & Data Science Platform

## Overview
This project automates the setup of cloud servers for web services, monitoring, and data science/ML with Ansible and Docker. It deploys NGINX, Prometheus, Node Exporter, Grafana, and Jupyter Notebook—all securely configured and managed.

## Features
- Automated server configuration and updates (Ansible)
- Docker installation and application deployment
- Secure admin user with SSH key-only access
- Live web server (NGINX)
- Monitoring stack: Node Exporter, Prometheus, Grafana
- Data science/ML workspace: Jupyter Notebook
- Sample ML notebook using scikit-learn, pandas, and matplotlib

## Access
- **NGINX:** http://your-droplet-ip
- **Prometheus:** http://your-droplet-ip:9090
- **Grafana:** http://your-droplet-ip:3000 (login: admin/admin)
- **Jupyter Notebook:** http://your-droplet-ip:8888
- **SSH admin:** `ssh -i ~/.ssh/id_ed25519 ansibleadmin@your-droplet-ip`
## How To Use
1. Clone this repo to your workstation.
2. Update the `hosts` file for your server IPs.
3. Run the setup:

ansible-playbook -i hosts setup.yml -u root --private-key=~/.ssh/id_ed25519

4. Upload and run data/ML notebooks in the Jupyter web UI.

## Demo ML Workflow
See `iris_ml_demo.ipynb`: loads the Iris dataset, trains a RandomForest model, and plots feature importance—a real, cloud-hosted ML example.

## Security
- Non-root admin user with key-only SSH access
- UFW firewall restricts traffic to only necessary ports

## Monitoring
- Node Exporter exports system stats
- Prometheus collects system metrics
- Grafana visualizes host performance in dashboards

## Portfolio/Interview Ready
This project demonstrates:
- Modern configuration management (Ansible)
- Production-ready security and service orchestration
- End-to-end cloud capabilities for infrastructure, monitoring, and ML/data science

---

