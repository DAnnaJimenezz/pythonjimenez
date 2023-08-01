import os

def ValidaciondeArchivos (funcionArchivo):
    try:
        with open (funcionArchivo, 'rt') as archivo:
            print ("Ya existe")
            print (len(archivo.readlines()))
    except IOError:        
        print ("Salio un error")
archivo = 'white1.txt'
funcionArchivo = "C:\\clon\\pythonjimenez\\ArchivosPython\\Archivo5\\white1.txt"
ValidaciondeArchivos (funcionArchivo)