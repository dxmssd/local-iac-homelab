.PHONY: deploy status destroy

deploy:
	@echo "Levantando Máquina Virtual con QEMU/KVM y Ansible..."
	vagrant up --provider=libvirt
	@echo "Desplegando Pods en K3s..."
	vagrant ssh -c "sudo k3s kubectl apply -f /vagrant/k8s/deployment.yaml"
	@echo "Laboratorio listo. Prueba ingresar a: http://192.168.121.10:30080"

status:
	vagrant status
	vagrant ssh -c "sudo k3s kubectl get pods,svc -A"

destroy:
	@echo "Eliminando Máquina Virtual y recursos..."
	vagrant destroy -f
