#!/usr/bin/env python3

import os, requests, time
import json, fileAdmin, re, sys

if (__name__== '__main__'):

    # Almacena contenido url pasada en el argumento
    url = str(sys.argv[1])

    # Hace petición GET a la url que le pasamos
    res = requests.get(url)

    # Si se conectó correctamente, descarga el contenido en un archivo JSON
    if(res.status_code == 200):
        response_json = json.loads(res.text)

        # codifica el contenido del JSON
        jsonFILE = json.dumps(response_json, indent = 4, separators = (',', ': '))

        # obtiene datos del servidor para salvar el archivo
        matchObj = re.match( r'(.*?\/\/)(.*?)(:.+)(\/resultado$)',url,0)

        if(matchObj):
            ip_address = matchObj.group(2)
        else:
            ip_address = "IP_desconocida"

        date = str(time.strftime('%Y-%m-%d'))
        path = os.getcwd()+"/"

        #salva el archivo JSON
        fileAdmin.saveFile(path,"<"+ip_address+">_<"+date+">.json",jsonFILE)

        print(">> Se ha exportado el archivo correctamente.\nDetalles: "+ path+"<"+ip_address+">_<"+date+">.json")

    else:
        print('>> Ha ocurrido un error al intentar conectarse.')
