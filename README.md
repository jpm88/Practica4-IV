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
