# Ejemplos de scripts de automatización. Introducción a OpenStack

## Escenario 1 (shell + ansible): Una instancia con wordpress

* escenario.sh: Script bash que crea una instancia, indicando los siguientes datos: imagen, red, sabor, grupo de seguridad, calve ssh y nombre.
* main.yaml: Receta ansible que despliega de forma automática una aplicación web Wordpress en la instancia creada anteriormente.
* del_escenario-sh: script bash, que borra la instancia y la ip flotante.

## Escenario 2 (python + ansible): Dos instancias (servidor de base de datos y servidor web) con wordpress

* escenario.py: Programa python que crea dos instancias, además abre el puerto 3128 en el grupo de seguridad "default". Asocia una ip flotante a cada instancia.
* main.yaml: Receta ansible que configura un servidor web en la primera instancia y un servidor mysql en la segunda. Además instala una aplicación web wordpress en el servidor web.
* del_escenario.py: Programa python que borra la infraestructura creada.

## Escenario 3 (shell): Creación automática de un escenario

<img src="http://iesgn.github.io/ow1/curso/u6/img/escenario4.png"7>

* demo.sh: Crea el escenario que tenemos en la imagen. Una vez ejecutado el script tendremos el escenario completamente configurado y operativo y podremos acceder a la instancia que tiene asociada una IP flotante y desde ella a las demás.
* demo-inv.sh: Elimina correctamente todos los elementos del escenario anterior.

## Escenario 4 (cloud-init): Creación de instancia con wordpress

* cloud-config.yaml: Fichero yaml cloud-config que instala un servidor web y mysql al crear una instancia y configura en ella la aplicación web wordpress.

Para acceder a la aplicación wordpres tenemos que utilizar la URL:
=======
### Ejemplo de uso

Vamos a crear una instancia que se llame wordpress:

		nova boot \
  		--image 'Debian 8.0' \
  		--key_name clave-ow \
  		--flavor ssd.XXS \
  		--user-data cloud-config-yaml \
  		--nic net-id=4f0dcc21-4b6c-47db-b283-591fdb9aa5a7 \
  		wordpress

  		nova floating-ip-associate wordpress 212.231.128.188

Para accder a la aplicación wordpres tenemos que acceder a la URL:


		http://wordpress.novalocal

Utilizando resolución estática, añadimos a /etc/hosts de nuestro equipo:

		212.231.128.188 wordpress.novalocal

## Escenario 5 (heat):