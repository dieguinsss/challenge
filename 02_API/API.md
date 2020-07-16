# API

API o interfaz para el envío y presentación de los datos recolectados.

### Pre-requisitos

Antes de la ejecutar el aplicativo verifique que la ruta de la variable de entorno en Linux sea la correcta.

```#!/usr/bin/env python3```

Por otra parte, si va a ejecutar el archivo directamente con como script desde la terminal, asegúrese que el archivo **02_API.py** disponga permisos de ejecución.

```
$ ls -la 02_API.py

-rwxr-xr-x 1 user group 1443 jul  7 11:56 02_API.py
```
En caso de que requiera asignar permisos, ejecute:

```$ chmod 764 02_API.py```

### Ejecución

Para su ejecución utilice la siguiente sentencia. En algunos casos podría variar el nombre del ejecutable de Python.

```$ ./02_API.py```

o

```$ python3 02_API.py```

Posteriormente acceder mediante el navegador al servidor, desde el local mediante la siguiente url:

```http://ip_de_servidor_central:5000/```

Esta presentará un mensaje de bienvenida "************ Bienvenido al Challenge ************".

### Construcción

A continuación se detalla brevemente la estructura del código.

***Librerías***
Inicialmente para su funcionamiento utiliza las libreras propias de Python
*os
*re
*time
*json


```
import os, re, time
import json, fileAdmin

```

Adicionalmente es preciso instalar y configura la librería Flask, como se indica en el Readme.md del proyecto.

```
from flask import Flask,request
```

En este caso se trata de un script muy sencillo que mediante Flask se levanta un servicio web publicado por default en el puerto 5000. El mismo se encarga de recibir los mensajes POST enviados por el agente a la url http://ip_de_servidor_central:5000/ y de almacenar en un archivo JSON, los resultados.

### FIN
