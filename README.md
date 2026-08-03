# local-iac-homelab
Un entorno de homelab local automatizado basado en **Infrastructure as Code (IaC)**.

[diagrama foto poner host]
[diagrama de red ]

Tecnologías Utilizadas

    - Host OS: CachyOS (Linux Kernel 7.x)

    - Orquestador de Infraestructura: Vagrant 2.x

    - Hipervisor: VirtualBox 7.x (Headless execution via Kernel Modules vboxdrv, vboxnetflt, vboxnetadp)

    - Gestor de Configuración: Ansible

    - Sistema Operativo Guest: Ubuntu 22.04 LTS (Jammy Jellyfish)


Requisitos Previos

En el sistema Host (Arch / CachyOS / Linux):

# Instalar dependencias esenciales
sudo pacman -S vagrant virtualbox ansible

# Cargar módulos del kernel para VirtualBox (Host-Only Networking)
sudo modprobe vboxdrv vboxnetadp vboxnetflt

Inicio Rápido

1. Clonar el repositorio:

git clone [https://github.com/dxmssd/local-iac-homelab.git](https://github.com/dxmssd/local-iac-homelab.git)
cd local-iac-homelab

2. Desplegar la infraestructura:


vagrant up --provider=virtualbox

3. Acceder a la VM por SSH:

vagrant ssh

4. Re-ejecutar el aprovisionamiento de Ansible:

vagrant provision

5. Destruir el entorno (Cleanup):

vagrant destroy -f




Estado del Proyecto & Próximos Pasos

    [x] Migración exitosa de proveedor a VirtualBox en CachyOS.

    [x] Configuración de red Host-Only e interfaces NAT.

    [x] Integración de Ansible Provisioner para instalación de herramientas base.

    [x] Implementación de roles en Ansible para K3s / Docker.

    [x] Escalado a topología de múltiples nodos (Control Plane + Worker Nodes).
