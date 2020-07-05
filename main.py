#!/usr/bin/env python3.6
import os, socket, time
import json, dicParser, fileAdmin

# setear ruta donde se van a recuperar los archivos.
path = "/home/diego/DES/code_py/MELI/src/"
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
dicMerge = {}
dicMerge.update(dicCPU)
dicMerge.update(dicPRC)
dicMerge.update(dicWHO)
dicMerge.update(dicVER)

# codifica el contenido del JSON
jsonFILE = json.dumps(dicMerge, indent = 4, separators = (',', ': '))

# obtiene datos del servidor para salvar el archivo
hostname = socket.gethostname()
ip_address =  socket.gethostbyname(hostname)
date = str(time.strftime('%Y-%m-%d'))

#salva el archivo JSON
fileAdmin.saveFile(path,"<"+ip_address+">_<"+date+">.json",jsonFILE)
