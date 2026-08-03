from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.onprem.iac import Ansible
from diagrams.onprem.client import User

# configuracion del tamano y del espacio
graph_attr = {
    "fontsize": "18",
    "bgcolor": "white",       # Fondo blanco
    "pad": "1.0",             # Margen exterior del recuadro principal 
    "nodesep": "1.2",         # Separa los nodos horizontalmente para expandir el diagrama
    "ranksep": "1.5",         # Separa los nodos verticalmente para hacerlo más alto
}

# Configuración específica para ampliar los cuadros/clústeres internos
cluster_attr = {
    "margin": "30",           # Espacio interno (padding) dentro de cada caja/Cluster
    "fontsize": "14",
}

with Diagram(
    "Local IaC Homelab Architecture", 
    show=False, 
    filename="architecture", 
    outformat="png", 
    graph_attr=graph_attr
):
    
    internet = Internet("Internet (NAT)")

    # Pasamos cluster_attr a los grupos para darles más margen interno
    with Cluster("Host OS: CachyOS (Linux Kernel)", graph_attr=cluster_attr):
        vagrant = User("Vagrant CLI")
        ansible = Ansible("Ansible Provisioner")
        vbox = Server("VirtualBox Hypervisor")

        with Cluster("Virtual Machine (Headless)", graph_attr=cluster_attr):
            vm_ubuntu = Server("Ubuntu 22.04 LTS\n(Guest Node)")

    # Flujo de trabajo
    vagrant >> Edge(label="1. Orquesta", color="darkblue") >> vbox
    vbox >> Edge(label="2. Despliega VM", color="darkgreen") >> vm_ubuntu
    
    vagrant >> Edge(label="3. Ejecuta", color="brown") >> ansible
    ansible >> Edge(label="4. Configura SSH", color="red", style="dashed") >> vm_ubuntu

    # Red
    vm_ubuntu >> Edge(label="Adapter 1: NAT", color="orange") >> internet