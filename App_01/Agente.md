# Agente

Es un script que permite de realizar un discovery y recolectar de los siguientes datos del servidor.

* Información sobre el procesador.
* Listado de procesos corriendo.
* Usuarios con una sesión abierta en el sistema.
* Nombre del sistema operativo.
* Versión del sistema operativo.

Y finalmente los resultados son almacenado en el mismo directorio en un archivo consolidado denominado **<IP de servidor>_<AAAA-MM-DD>.json**

### Pre-requisitos

Antes de la ejecutar el aplicativo verifique que la ruta de la variable de entorno en Linux sea la correcta.

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

```$ ./01_agente.py```

o

```$ python3 01_agente.py```

Si todo ha corrido bien el script debería dejar los siguientes archivos en el directorio.
```
-rw-r--r-- 1 user group 89433 jul  9 17:29  '<127.0.1.1>_<2020-07-09>.json'
-rw-r--r-- 1 user group  4412 jul  9 17:29  output0.txt
-rw-r--r-- 1 user group 36414 jul  9 17:29  output1.txt
-rw-r--r-- 1 user group   310 jul  9 17:29  output2.txt
-rw-r--r-- 1 user group   105 jul  9 17:29  output3.txt
```

### Construcción

A continuación se detalla brevemente la estructura del código.

***Librerías***
Inicialmente para su funcionamiento utiliza las libreras propias de Python
*os
*socket
*time
*json

```
#!/usr/bin/env python3
import os, socket, time
import json, dicParser, fileAdmin
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

Función utilizada para parsear los datos del archivo 'output0.txt', este contiene la ***Información sobre el procesador***

```dicParser.getColsValsCPU(path, filename)```

Listado de procesos corriendo.
Usuarios con una sesión abierta en el sistema.
Nombre del sistema operativo.
Versión del sistema operativo


```dicParser.getColsValsPRC(path, filename)```

```dicParser.getColsValsWHO(path, filename)```

```dicParser.getColsValsVER(path, filename)```

```dicParser.setDictionary(size, cols, values, flag)```


```saveFile(path, filename, data)```


```saveFile(path, filename, data)```

```saveFile(path, filename, data)```
```
# parsea los contenidos recolectados
colsCPU, valuesCPU, sizeCPU, flagCPU = dicParser.getColsValsCPU(path,'output0.txt')
colsPRC, valuesPRC, sizePRC, flagPRC = dicParser.getColsValsPRC(path,'output1.txt')
colsWHO, valuesWHO, sizeWHO, flagWHO = dicParser.getColsValsWHO(path,'output2.txt')
colsVER, valuesVER, sizeVER, flagVER = dicParser.getColsValsVER(path,'output3.txt')

# configura los diccionarios de datos con la información recoletada
dicCPU = dicParser.setDictionary(sizeCPU, colsCPU, valuesCPU, flagCPU)
dicPRC = dicParser.setDictionary(sizePRC, colsPRC, valuesPRC, flagPRC)
dicWHO = dicParser.setDictionary(sizeWHO, colsWHO, valuesWHO, flagWHO)
dicVER = dicParser.setDictionary(sizeVER, colsVER, valuesVER, flagVER)

# consolida los diccionarios
dicMerge = {'cpu' : dicCPU,'procesos' : dicPRC, 'who:' : dicWHO, 'version' : dicVER}

# codifica el contenido del JSON
jsonFILE = json.dumps(dicMerge, indent = 4, separators = (',', ': '))

# obtiene datos del servidor para salvar el archivo
hostname = socket.gethostname()
ip_address =  socket.gethostbyname(hostname)
date = str(time.strftime('%Y-%m-%d'))

#salva el archivo JSON
fileAdmin.saveFile(path,"<"+ip_address+">_<"+date+">.json",jsonFILE)
```
,mn,n
