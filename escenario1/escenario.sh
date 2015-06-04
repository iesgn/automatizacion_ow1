#!/bin/bash

IMAGEN='5e3a5ae7-cee5-41ab-9f4a-8289044da1a5'
RED='00000335-net'
CLAVE='clave-ow'
SEGURIDAD='default'
SABOR='ssd.XXXS'
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
echo "# Pasados unos instantes estará creado el escenario completo y podrás acceder #"
echo "# a $NOMBRE con:                                                              #"
echo "#                                                                             #"
echo "# ssh -i .ssh/$CLAVE debian@$IP                                             #"
echo "#                                                                             #"
echo "###############################################################################"