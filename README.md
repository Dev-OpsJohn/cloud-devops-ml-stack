# GPU Ansible Automation

This repository contains Ansible playbooks, roles, and supporting files for managing GPU infrastructure, automation, and monitoring.

## Project Structure

- `ansible/`       – Playbooks, roles, inventories for server automation
- `monitoring/`    – Monitoring stack (Prometheus, Grafana, exporters)
- `terraform/`     – Terraform infrastructure code
- `docs/`          – Documentation (architecture, usage, changelog)
- `scripts/`       – Support scripts

## Requirements

- Ansible 2.9+
- Docker (for monitoring stack)
- Terraform (for IaaS automation)
- Compatible Linux OS

## Monitoring & Dashboards

Grafana dashboards for monitoring GPU nodes are stored in:

monitoring/grafana/dashboards/


The project includes:

- `sample-dashboard.json` – Example and template dashboard.
- `gpu-bare-metal-automation-dashboard.json` – GPU Bare Metal Automation Project dashboard for Grafana.

### Importing Dashboards to Grafana

1. Open Grafana and go to "Dashboards" → "Manage".
2. Click "Import" in the top/right.
3. Upload the dashboard JSON file from `monitoring/grafana/dashboards/` or paste its contents.
4. Complete the import, assigning appropriate data sources as prompted.

## Setup

1. **Clone the Repo**

git clone https://github.com/your-username/gpu-ansible.git
cd gpu-ansible


2. **Configure Inventory & Vars**
- Edit inventory and variables in `ansible/` as required for your environment.

3. **Run Ansible Playbooks**
- Example:
  ```
  ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/base-setup.yml
  ```

4. **Deploy Monitoring Stack**
- From `monitoring/`, use Docker Compose:
  ```
  cd monitoring
  docker-compose up -d
  ```

## Documentation

See the `docs/` folder for:

- `architecture.md` – System architecture overview
- `changelog.md`    – Release notes and changes
- `usage.md`        – How to use playbooks, monitoring, Terraform modules

## Contributing

Contributions, issues, and feature requests are welcome. Please update docs if you add new dashboards, roles, or features.

## License

See `LICENSE` for details.

