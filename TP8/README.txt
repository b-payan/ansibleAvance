install molecule (necessite docker sur la machine)
pipx install molecule
cd TP8/tp8.wordpress
molecule init scenario
molecule converge
molecule test


lancement du playbook
ansible-playbook -i inventory/host playbook/tp4.yml

Test
docker --version

