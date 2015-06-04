#!/bin/sh

NOMBRE="pc1"

# Obtengo la ip flotante asociada a la instancia

INSTANCIA_ID=$(nova list|grep pc1|awk '{print $2}')
IP_FLOTANTE=$(nova floating-ip-list|grep $INSTANCIA_ID|awk '{print $2}')

# Borramos el servidor

nova delete $NOMBRE

# Liberamos la IP flotante

nova floating-ip-delete $IP_FLOTANTE