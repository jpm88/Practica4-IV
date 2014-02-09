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

Para la realización de esta práctica vamos a montar una máquina virtual sobre nuestro sistema, usando VirtualBox, crearemos una nueva imagen de Ubuntu, en ella trabajaremos con PHP para utilizar una aplicación realizada en la asignatura de TW y se colgará en OpenShift para su visualización.

#### Creación de la máquina virtual

Vamos a crear una máquina con VirtualBox, empezamos eligiendo el SO que queremos instalar:

![img1](https://raw2.github.com/jpm88/Practica4-IV/master/imagenes/img1.jpg)

Le asignamos la memoria RAM que necesitemos:

![img2](https://raw2.github.com/jpm88/Practica4-IV/master/imagenes/img2.jpg)

Y creamos nuestro disco duro virtual:

![img3](https://raw2.github.com/jpm88/Practica4-IV/master/imagenes/img3.jpg)

Terminamos los pasos y se iniciará la instalación de Ubuntu, una vez terminada ya lo tendremos listo para trabajar:

![img4](https://raw2.github.com/jpm88/Practica4-IV/master/imagenes/img4.jpg)


#### Explicación del funcionamiento de la aplicación

La aplicación que se va a usar es una

#### Utilizando OpenShift

Nos creamos una cuenta en https://www.openshift.com/ y le damos a "Add application", nos saldrá la siguiente pantalla:

![img5](https://raw2.github.com/jpm88/Practica4-IV/master/imagenes/img5.jpg)

Como nuestra aplicación está hecha en PHP elegimos esa opción.

Ahora creamos la aplicación con los siguientes datos:

![img6](https://raw2.github.com/jpm88/Practica4-IV/master/imagenes/img6.jpg)

Una vez creado el proyecto pasamos a copiarlo a nuestro pc, usando la dirección que OpenShift nos ofrece para clonar directorios a nuestro pc a través de SSH:

    git clone ssh://52643eeb5973ca7db20000c7@practica1-jpm88.rhcloud.com/~/git/practica1.git/

Una vez tengamos el directorio en nuestro pc, añadimos los archivos de nuestro periódico digital en la carpeta php, ahora toca subirla, con los siguientes comando:

    git add -A
    git commit -a -m "Practica 4 de IV"
    git push origin master
    
Y ya tendríamos la práctica subida en la siguiente dirección:

http://practica1-jpm88.rhcloud.com/

No consigo que se me abra correctamente desde el enlace:

![img7](https://raw2.github.com/jpm88/Practica4-IV/master/imagenes/img7.jpg)

Después toqué algo y volví a hacer push y ya no me funcionaba desde el enlace, y no he conseguido arreglarlo.









