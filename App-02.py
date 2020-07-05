#!/usr/bin/env python3

import os, re
import json
from flask import Flask

# setear ruta donde se van a recuperar los archivos.
path = os.getcwd()+"/"
#busca los archivos
dir = os.listdir(path)

# busca el archivo JSON
for d in dir:
    matchObj = re.match(r'^(.*.json)',d,0)
    if (matchObj):
        filename = matchObj.group(1)
        fo = open(path+filename,'r')
        #decodifica y lee el JSON
        data = json.loads(fo.read())
        fo.close()

# importa el objeto y crea la instancia del módulo flask
app = Flask(__name__)

# se crean las rutas adonde responderá el servidor
@app.route('/')
def index():
    return "Bienvenido al Challenge de Mercado Libre"

# se crean las rutas adonde responderá el servidor. En la ruta resultado se
# obtiene el archivo JSON

@app.route('/resultado', methods=['GET'])
def get():
    return data

if( __name__ == "__main__"):
    app.run(debug = True)
