# Endpoint

En este caso se trata de un script que se conecta a la API del servidor y permite descargar la información desde una computadora cliente conectada a la red, de forma remota.
Al finalizar los resultados son almacenados en un archivo consolidado denominado **<IP de servidor>_<AAAA-MM-DD>.json**

### Pre-requisitos

Antes de la ejecutar el aplicativo verifique que la ruta de la variable de entorno en Linux sea la correcta.

```#!/usr/bin/env python3```

Por otra parte, si va a ejecutar el archivo directamente con como script desde la terminal, asegúrese que el archivo **03_endpoint.py** disponga permisos de ejecución.

```
$ ls -la 03_endpoint.py

-rwxr-xr-x 1 user group 1443 jul  7 11:56 03_endpoint.py
```
En caso de que requiera asignar permisos, ejecute:

```$ chmod 764 03_endpoint.py```

### Ejecución

Para su ejecución, utilice la siguiente sentencia. En algunos casos podría variar el nombre del ejecutable de Python.

```$ ./03_endpoint.py 'http://localhost:5000/resultado' ```

o

```$ python3 03_endpoint.py 'http://localhost:5000/resultado'```

Para el argumento 'http://localhost:5000/resultado', deberá ser ajustar el host (localhost) a la ip del servidor que corresponda.

Si todo ha corrido bien el script debería dejar el siguiente archivos en el directorio.
```
-rw-r--r-- 1 user group 89433 jul  9 17:29  '<127.0.1.1>_<2020-07-09>.json'
```

### Construcción

A continuación se detalla una breve explicación del código. 
Se trata de una estructura sencilla en la cual el proceso recibe una variable 'argumento' con el host adonde se debe conectar. Posteriormente, descarga el contenido JSON y por último almacena el archivo con el nombre del servidor y la fecha actual.

***Librerías***
Inicialmente para su funcionamiento utiliza las libreras propias de Python
*os
*requests
*sys
*time
*json
*re

```
#!/usr/bin/env python3
import os, requests, time
import json, fileAdmin, re,sys
```

Adicionalmente utiliza el módulo **fileAdmin**, donde aprovecha la función

```saveFile(path, filename, data)```

para salvar el archivo <IP>_<YYYY-MM-DD>.json


### FIN
