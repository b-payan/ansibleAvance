install du role
ansible-galaxy install -r requirements.yml --force

lancement du playbook
ansible-playbook -i inventory/host tp6.yml --tags mysql
ansible-playbook -i inventory/host tp6.yml --tags wordpress

Test
cat /etc/last_changed

Connection a wordpress
http://localhost/

