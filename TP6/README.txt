install du role
ansible-galaxy install -r requirements.yml --force

lancement du playbook
ansible-playbook -i inventory/host tp6.yml --tags mysql
ansible-playbook -i inventory/host tp6.yml --tags wordpress

Test
cat /etc/last_changed

Connection a wordpress
http://localhost/

Mise en place du vault:
ansible-vault encrypt vaults/db_secret.yml
New Vault password: P@ssword

Execution playbook, avec vault :
ansible-playbook -i inventory/host tp6.yml --ask-vault-password 

