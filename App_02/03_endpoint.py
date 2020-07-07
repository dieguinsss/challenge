#!/usr/bin/env python3

import os, requests, time
import json, fileAdmin, re

if (__name__== '__main__'):
    url = 'http://localhost:5000/resultado'

    res = requests.get(url)
    print(res.url)

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
