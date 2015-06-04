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
    return d

# Me conecto al cloud
nova = client.Client(**get_nova_creds())

server=nova.servers.find(name=nombre1)
# Selecciono la ip flotente 
ip_flotante =  server.networks.items()[0][1][1]
# elimino la instancia
server.delete()

nova.floating_ips.delete(nova.floating_ips.find(ip=ip_flotante))




