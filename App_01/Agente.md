# Agente

Es un script que permite de realizar un discovery y recolectar de los datos del servidor.

En el mismo se encuentran alojados 3 aplicativos:

1. [**Agente**](https://github.com/dieguinsss/challenge/blob/master/App_01/Agente.md)- Es un script que permite de realizar un discovery y recolectar de los datos del servidor.
2. [**API**](https://github.com/dieguinsss/challenge/blob/master/App_01/API.md) - Se trata de un API o interfaz para el envío y presentación de los datos recolectados.
3. [**Endpoint**](https://github.com/dieguinsss/challenge/blob/master/App_02/03_endpoint.py) - Es un script para recolectar la información mediante desde una computadora cliente en la red.
```
#!/usr/bin/env python3
import os, socket, time
import json, dicParser, fileAdmin

# setear ruta donde se van a recuperar los archivos.
path = os.getcwd()+"/"
#realiza el descubrimiento y recolección de los datos
fileAdmin.discovery()

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
