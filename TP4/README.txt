install du role
ansible-galaxy install -r requirements.yml --force

lancement du playbook
ansible-playbook -i inventory/host playbook/tp4.yml

Test
docker --version

