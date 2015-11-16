#!/bin/bash

IMAGEN='7db71d85-4e13-419c-8d12-ed4e9fc01cba'
RED='red'
CLAVE='clave-openstack'
SEGURIDAD='default'
SABOR='local.XXS'
NOMBRE="pc1"

# Obtenemos el id de la red

NET_ID=$(nova net-list|grep $RED|awk '{print $2}')

## Creamos la instancia llamada NOMBRE conectada a la red,con la clave, sabor y regla de seguridad indicadas

nova boot --flavor $SABOR --image $IMAGEN \
            --security-groups $SEGURIDAD\
	    --key-name $CLAVE \
            --nic net-id=$NET_ID \
            $NOMBRE

## Asignamos una IP flotante a la instancia

IP=$(nova floating-ip-create ext-net|awk 'NR==4'|awk '{print $2}')
echo 'IP flotante asignada '$IP
nova floating-ip-associate $NOMBRE $IP


echo ""
echo "###############################################################################"
echo " Pasados unos instantes estará creado el escenario completo y podrás acceder   "
echo " a $NOMBRE con:                                                                "
echo ""
echo " ssh -i ~/.ssh/$CLAVE debian@$IP"
echo ""
echo "###############################################################################"

STATUS=$(nova show $NOMBRE|grep status|awk '{print $4}')
while [ "$STATUS" != "ACTIVE" ]
do
	echo "$STATUS"
	sleep 10;
	STATUS=$(nova show $NOMBRE|grep status|awk '{print $4}')
done

echo "Ejecutando receta ansible..."
echo "[servidores]>hosts"
echo "$NOMBRE ansible_ssh_host=$IP ansible_ssh_user=debian">>hosts
#ansible-playbook main.yml

