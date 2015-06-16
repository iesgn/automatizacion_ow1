# Ejemplos de scripts de automatización. Introducción a OpenStack

## Escenario 1: Una instancia con wordpress

* escenario.sh: Script bash que despliega una instancia, indicando los siguientes datos: imagen, red, sabor, grupo de seguridad, calve ssh y nombre.
* main.yaml: Receta ansible que despliega de forma automática una aplicación web Wordpress en la instancia creada anteriormente.
* del_escenario-sh: script bash, que borra la instancia y la ip flotente.

## Escenario 2: Dos instancias (servidor de base de datos y servidor web) con wordpress