#
# Este módulo contiene las fuciones parsear los contenidos obtenidos y setear
# los diccionarios de datos para crear el JSON final.
#

import re

# función para parsear informacion de CPU (cat /proc/cpuinfo)
def getColsValsCPU(path, filename):
    input = open(path+filename).readlines()
    cols = []
    values = []
    flag = 0

    for i in input:
        i = i.split(':')
        if (len(i)>1):
            cols.append(i[0].replace('\t','').replace(' ','_'))
            values.append(str(i[1]))

    size = cols.count("processor")
    return cols, values, size, flag

# función para parsear informacion de procesos corriendo (ps -ax)
def getColsValsPRC(path, filename):
    input = open(path+filename).readlines()
    counter = 0
    cols = []
    values = []
    flag = 1

    for i in input:
        matchObj = re.match( r'\s*(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\n',i,0)
        if(counter == 0):
            cols.append(matchObj.group(1))
            cols.append(matchObj.group(2))
            cols.append(matchObj.group(3))
            cols.append(matchObj.group(4))
            cols.append(matchObj.group(5))
            counter = counter + 1
        else:
            values.append(matchObj.group(1))
            values.append(matchObj.group(2))
            values.append(matchObj.group(3))
            values.append(matchObj.group(4))
            values.append(matchObj.group(5))

    size = len(input)
    return cols, values, size, flag

# función para parsear informacion de usuarios activos (w)
def getColsValsWHO(path, filename):
    input = open(path+filename).readlines()
    counter = 0
    cols = []
    values = []
    flag = 1

    for i in input:
        matchObj = re.match( r'\s*(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\n',i,0)
        if(counter == 0):
            counter = counter + 1
        elif(counter == 1):
            cols.append(matchObj.group(1))
            cols.append(matchObj.group(2))
            cols.append(matchObj.group(3))
            cols.append(matchObj.group(4))
            cols.append(matchObj.group(5))
            cols.append(matchObj.group(6))
            cols.append(matchObj.group(7))
            cols.append(matchObj.group(8))
            counter = counter + 1
        else:
            values.append(matchObj.group(1))
            values.append(matchObj.group(2))
            values.append(matchObj.group(3))
            values.append(matchObj.group(4))
            values.append(matchObj.group(5))
            values.append(matchObj.group(6))
            values.append(matchObj.group(7))
            values.append(matchObj.group(8))

    size = len(input)-1
    return cols, values, size, flag

# función para parsear informacion de versión de sistema opera (uname -a)
def getColsValsVER(path, filename):
    input = open(path+filename).readlines()
    counter = 0
    cols = ['kernel_name','hostname','version','system','date','hw','processor', 'os']
    values = []
    flag = 1

    for i in input:
        matchObj = re.match( r'\s*(.*?)\s+(.*?)\s+(.*?)\s+(.*)\s+(.*Linux$)',i,0)
        values.append(matchObj.group(1))
        values.append(matchObj.group(2))
        values.append(matchObj.group(3))
        values.append(matchObj.group(4))
        values.append(matchObj.group(5))
        values.append(matchObj.group(6))
        values.append(matchObj.group(7))
        values.append(matchObj.group(8))

    size = len(input)+1

    return cols, values, size, flag

# función para configurar diccionarios de datos con la información parseada
def setDictionary(size, cols, values, flag):
    dic = {}
    counter = 0

    for i in range(size-1):
        dic[i] = {}
        for col in range(len(cols)):
            dic[i][cols[col]] = ''

    if(flag == 0): #procesa información de CPU -- flag = 0
        for j in range(len(dic)):
            for k in (dic[j]):
                dic[j][k] = values[counter].replace('\n','')
                counter = counter + 1
    elif(flag == 1): #procesa información de procesos, usuarios conectados, versión -- flag = 1
        for j in range(len(dic)):
            for k in (dic[j]):
                dic[j][k] = values[counter]
                counter = counter + 1
    else:
        print(">> Error en la configuracion del diccionario.")

    return dic
