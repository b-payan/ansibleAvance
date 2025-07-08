install du role
ansible-galaxy install -r requirements.yml --force

lancement du playbook
ansible-playbook -i inventory/host playbook/tp5.yml

Test
cat /etc/last_changed

