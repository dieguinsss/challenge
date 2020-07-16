#!/usr/bin/env python3

import os, re, time
import json, fileAdmin
from flask import Flask,request

# importa el objeto y crea la instancia del módulo flask
app = Flask(__name__)

# se crean las rutas adonde responderá el servidor
@app.route('/')
def index():
    return "************ Bienvenido al Challenge ************"

@app.route('/resultado', methods=['POST'])
def dataSrv():
    if(request.method == 'POST'):

        data = request.get_data()
        data_json = json.loads(data)

        # codifica el contenido del JSON
        jsonFILE = json.dumps(data_json, indent = 4, separators = (',', ': '))

        print(">> Source: ", request.remote_addr)
        print(">> Date: ", str(time.strftime('%Y-%m-%d')))
        print(">> Path: ", str(os.getcwd()+"/"))
        fileAdmin.saveFile(str(os.getcwd()+"/"),str(request.remote_addr)+"_"+str(time.strftime('%Y-%m-%d'))+".json", jsonFILE)
        return '>> Resultado enviado...'
    else:
        return '>> Ha ocurrido un error...'


if( __name__ == "__main__"):
    app.run(host = '0.0.0.0')
