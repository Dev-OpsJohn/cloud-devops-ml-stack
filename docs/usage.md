# Usage

1. Clone the repository.
2. Set up Ansible and Terraform prerequisites.
3. Configure your `ansible/inventory/hosts.yml` for your cluster.
4. Run `ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/base-setup.yml`.
5. Start monitoring with `docker-compose up` in the `monitoring` directory.
