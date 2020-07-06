#!/usr/bin/env python3

import os, re
import json
from flask import Flask

# busca el archivo JSON
def getJSON():
    # setear ruta donde se van a recuperar los archivos.
    path = os.getcwd()+"/"
    #busca los archivos
    dir = os.listdir(path)
    data = {}

    for d in dir:
        matchObj = re.match(r'^(.*.json)',d,0)
        if (matchObj):
            filename = matchObj.group(1)
            fo = open(path+filename,'r')
            #decodifica y lee el JSON
            data[d] = json.loads(fo.read())
            fo.close()

    return data

# importa el objeto y crea la instancia del módulo flask
app = Flask(__name__)
data = getJSON()

# se crean las rutas adonde responderá el servidor
@app.route('/')
def index():
    return "************ Bienvenido al Challenge ************"

# se crean las rutas adonde responderá el servidor. En la ruta resultado se
# obtiene el archivo JSON

@app.route('/resultado', methods=['GET'])
def get():
    if(data):
        return data
    else:
        return ">> No se han encontrado archivos"

if( __name__ == "__main__"):
    app.run(debug = True)
