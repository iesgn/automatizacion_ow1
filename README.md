# Ejemplos de scripts de automatización. Introducción a OpenStack

## Escenario 1: Una instancia con wordpress

* escenario.sh: Script bash que crea una instancia, indicando los siguientes datos: imagen, red, sabor, grupo de seguridad, calve ssh y nombre.
* main.yaml: Receta ansible que despliega de forma automática una aplicación web Wordpress en la instancia creada anteriormente.
* del_escenario-sh: script bash, que borra la instancia y la ip flotente.

## Escenario 2: Dos instancias (servidor de base de datos y servidor web) con wordpress

* escenario.py: Programa python que crea dos instancias, además abre el puerto 3128 en el grupo de seguridad "default". Asocia una ip flotante a cada instancia.
* main.yaml: Receta ansible que configura un servidor web en la primera instancia y un servidor mysql en la segunda. Además instala una aplicación web wordpress en el servidor web.
* del_escenario.py: Programa python que borra la infraestructura creada.

## Escenario 3: Creación automática de un escenario

<img src="http://iesgn.github.io/ow1/curso/u6/img/escenario4.png"7>

* demo.sh: Crea el escenario que tenemos en la imágen. Una vez ejecutado el script tendremos el escenario completamente configurado y operativo y podremos acceder a la instancia que tiene asociada una IP flotante y desde ella a las demás.
* demo-inv.sh: Elimina correctamente todos los elementos del escenario anterior.