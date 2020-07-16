# Agente

Es un script que permite de realizar un discovery y recolectar de los siguientes datos del servidor.

* Información sobre el procesador.
* Listado de procesos corriendo.
* Usuarios con una sesión abierta en el sistema.
* Nombre del sistema operativo.
* Versión del sistema operativo.

Al finalizar envia los datos al servidor central en formato JSON.

### Pre-requisitos

Antes de ejecutar el aplicativo verifique que la ruta de la variable de entorno en Linux sea la correcta.

```#!/usr/bin/env python3```

Por otra parte, si va a ejecutar el archivo directamente con como script desde la terminal, asegúrese que el archivo **01_agente.py** disponga permisos de ejecución.

```
$ ls -la 01_agente.py

-rwxr-xr-x 1 user group 1443 jul  7 11:56 01_agente.py
```
En caso de que requiera asignar permisos, ejecute:

```$ chmod 764 01_agente.py```

### Ejecución

Para su ejecución utilice la siguiente sentencia. En algunos casos podría variar el nombre del ejecutable de Python.

```$ ./01_agente.py http://ip_de_servidor_central:5000/resultado```

o

```$ python3 01_agente.py http://ip_de_servidor_central:5000/resultado```

Si todo ha corrido bien el script debería dejar los siguientes archivos en el directorio.
```
-rw-r--r-- 1 user group  4412 jul  9 17:29  output0.txt
-rw-r--r-- 1 user group 36414 jul  9 17:29  output1.txt
-rw-r--r-- 1 user group   310 jul  9 17:29  output2.txt
-rw-r--r-- 1 user group   105 jul  9 17:29  output3.txt
```
y enviar el contenido al servidor destino


### Construcción

A continuación se detalla brevemente la estructura del código.

***Librerías***
Inicialmente para su funcionamiento utiliza las libreras propias de Python
*os
*time
*json
*requests
*sys

```
#!/usr/bin/env python3
import os, time
import json, dicParser, fileAdmin
import requests, sys
```

Adicionalmente a estas se han creado 2 módulos adicionales localizados en el mismo directorio para segmentar el código y se explican abajo.
*dicParser
*fileAdmin

**fileAdmin**
Este módulo contiene la funciones para llevar a cabo el descubrimiento de la información del sistema

```fileAdmin.discovery()```

y también, para almacenar los archivos resultantes en el servidor local.

```saveFile(path, filename, data)```

**dicParser**
Este módulo dispone las funciones para llevar a cabo el parseo de los datos recolectados y la construccin de los dicionarios.

Función utilizada para parsear los datos del archivo 'output0.txt', este contiene la ***Información sobre el procesador***.

```getColsValsCPU(path, filename)```

Función utilizada para parsear los datos del archivo 'output1.txt', este contiene un ***Listado de los procesos corriendo***.

```getColsValsPRC(path, filename)```

Función utilizada para parsear los datos del archivo 'output2.txt', este contiene la lista de ***Usuarios con una sesión abierta en el sistema***.

```getColsValsWHO(path, filename)```

Función utilizada para parsear los datos del archivo 'output3.txt', este contiene el detalle acerca del ***Nombre del sistema operativo*** y la ***Versión del sistema operativo***.

```getColsValsVER(path, filename)```

Función utilizada para configurar los diccionarios con la información parseada.

```setDictionary(size, cols, values, flag)```

### FIN
