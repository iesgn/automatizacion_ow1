#!/usr/bin/env python
from novaclient.v1_1 import client
import os,sys
import time

imagen="ej_ubuntu_update"
red='red'
clave='clave-ow'
seguridad='default'
sabor='ssd.XS'
nombre1="servidor_web"
nombre2="servidor_mysql"
def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    d['region_name']=os.environ['OS_REGION_NAME']
    return d

# Me conecto al cloud
nova = client.Client(**get_nova_creds())

# Selecciono la imagen
image = nova.images.find(name=imagen)

# Selecciono la red
network = nova.networks.find(label=red)

# Selecciono sabor
flavor = nova.flavors.find(name=sabor)

# Selecciono clave
keypair=nova.keypairs.find(name=clave)

# Selecciono red
network = nova.networks.find(label=red)


server1 = nova.servers.create(name = nombre1,image = image.id,flavor = flavor.id,nics =[{'net-id': network.id}] ,key_name = keypair.name,)

status = server1.status
sys.stdout.write('Building...')
while status == 'BUILD':
	time.sleep(1)
	sys.stdout.write(".")
	sys.stdout.flush()
	# Retrieve the instance again so the status field updates
	server1 = nova.servers.get(server1.id)
	status = server1.status

# Resevo una ip flotante
floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name)

server1.add_floating_ip(floating_ip)

print "Instancia %s creada y activa... con la ip %s"%(nombre1,floating_ip.ip)
ip1=floating_ip.ip


server2 = nova.servers.create(name = nombre2,image = image.id,flavor = flavor.id,nics =[{'net-id': network.id}] ,key_name = keypair.name)
server2.security_groups.append(nova.security_groups.find(name="default"))

status = server2.status
sys.stdout.write('Building...')
while status == 'BUILD':
	time.sleep(1)
	sys.stdout.write(".")
	sys.stdout.flush()
	# Retrieve the instance again so the status field updates
	server2 = nova.servers.get(server2.id)
	status = server2.status

# Resevo una ip flotante
floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name)

server2.add_floating_ip(floating_ip)

print "Instancia %s creada y activa... con la ip %s"%(nombre2,floating_ip.ip)
ip2=floating_ip.ip

fhost=open("hosts","w")
fhost.write("[servidores_web]\n%s ansible_ssh_host=%s ansible_ssh_user=ubuntu\n[servidor_mysql]\n%s ansible_ssh_host=%s ansible_ssh_user=ubuntu"%(nombre1,ip1,nombre2,ip2))
fhost.close()
os.system("ansible-playbook main.yml")
