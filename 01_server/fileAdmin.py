# Este módulo contiene las funciones para ejecuar los comandos en linux y obtener
# la información solicitada. A continuación se detalla la misma y los comandos
# utilizados.
#
# - Información sobre el procesador. (cat /proc/cpuinfo')
# - Listado de procesos corriendo. (ps -ax)
# - Usuarios con una sesión abierta en el sistema. (w)
# - Nombre del sistema operativo. (uname -a)
# - Versión del sistema operativo. (uname -a)
#
# función para recolectar la información del sistema operativo. Principalemnte
# se encarga de ejecutar los comandos requeridos.

import os

def discovery():
    cmdlist = ['cat /proc/cpuinfo','ps -ax', 'w', 'uname -a']
    i = 0

    for cmd in cmdlist:
        print("\n############## " + cmd + " ##############\n")

        os.system (cmd + ' > output' + str(i) + '.txt') #debugging
        os.system ('cat output' + str(i) + '.txt')
        i = i + 1
        print("\n################################\n")

    return

def saveFile(path, filename, data):
    fileOutput = open(path+filename,"w")
    fileOutput.write(data)
    fileOutput.close()
