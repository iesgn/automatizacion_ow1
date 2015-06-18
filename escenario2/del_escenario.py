#!/usr/bin/env python
from novaclient.v1_1 import client
import os,sys
import time

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

#secgroup = nova.security_groups.find(name="default")
#nova.security_group_rules.delete(secgroup.id,ip_protocol="tcp",from_port="3128",to_port="3128",cidr="0.0.0.0/0")
for nomserver in [nombre1,nombre2]:

	server=nova.servers.find(name=nomserver)
	# Selecciono la ip flotente 
	ip_flotante =  server.networks.items()[0][1][1]
	# elimino la instancia
	server.delete()
	nova.floating_ips.delete(nova.floating_ips.find(ip=ip_flotante))
	print "Delete %s" % nomserver




