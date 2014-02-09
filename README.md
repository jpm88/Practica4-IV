# Documentación Práctica 4: Diseño del soporte virtual al desarrollo y despliegue de una aplicación

## Juan Antonio Pérez Maldonado

## Licencia de la aplicación: GPLv3


### Explicación de la práctica

En la asignatura se ha visto como crear usar máquinas virtuales completas y como provisionar las aplicaciones y servicios necesarios y hacerlo de forma ágil y reproducible. El ciclo de desarrollo de un devops es el siguiente

* Provisionamiento para desarrollo.
* Provisionamiento de las máquinas de prueba (staging) y de producción.
* Configuración del despliegue del desarrollo a las máquinas de staging y eventualmente a las de producción.

Lo que se pretende con este ciclo es que el tiempo que pasa desde la incorporación de un nuevo desarrollador a un equipo hasta que es capaz de pasar a producción el desarrollo sea lo menor posible, de forma que el uso de recursos y el despliegue de los mismos sea un proceso ágil. Previo a tal proceso estará la elección de tales entornos de desarrollo y producción y el test de los mismos, pero en el momento qeu se comience el desarrollo, o paralelamente al mismo, las decisiones deben estar tomadas y las máquinas virtuales testeadas y provisionadas, con todas las configuraciones preparadas y almacenadas en un repositorio.

### Realización de la práctica

#### Introducción

Para la realización de esta práctica vamos a montar una máquina virtual sobre nuestro sistema, usando VirtualBox, crearemos una nueva imagen de Ubuntu, en ella trabajaremos con Python para utilizar una aplicación realizada en la asignatura de DAI y se colgará en OpenShift para su visualización.

#### Creación de la máquina virtual

Vamos a crear una máquina con VirtualBox, empezamos eligiendo el SO que queremos instalar:

![img1]()

Le asignamos la memoria RAM que necesitemos:

![img2]()

Y creamos nuestro disco duro virtual:

![img3]()

Terminamos los pasos y se iniciará la instalación de Ubuntu, una vez terminada ya lo tendremos listo para trabajar:

![img4]()


#### Explicación del funcionamiento de la aplicación

La aplicación que se va a utilizar es un "popurrí" de cosas que se han ido probando a lo largo de la asignatura de DAI:

- Uso de web.py.
- Plantillas mako
- Control de sesiones con MongoDB (pymongo)
- Formulario de registro con sus respectivas validaciones.
- Uso de feedparser
- Tweepy (Twitter en Python)
- Mapas de Google

La aplicación en si está un poco "verde" y desordenada.

#### Utilizando OpenShift

Nos creamos una cuenta en https://www.openshift.com/ y le damos a "Add application", nos saldrá la siguiente pantalla:

![img5]()

Como nuestra aplicación está hecha en Python 3.3 elegimos esa opción.

Ahora creamos la aplicación con los siguientes datos:

![img6]()




