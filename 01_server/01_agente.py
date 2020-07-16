#!/usr/bin/env python3
import os, time
import json, dicParser, fileAdmin
import requests, sys

# EJEMPLOS
# curl -X POST -d 'hola' http://localhost:5000/resultado
# curl -X POST -d '{name: diego, age: 37}' -H 'Content-Type: application/json' http://localhost:5000/resultado
#
url = str(sys.argv[1])

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

#envia JSON al agente
r = requests.post(url, data = jsonFILE)
print(r.text)
