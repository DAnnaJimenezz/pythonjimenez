import os 
def ValidaciondeArchivo (funcionArchivo):
    try:
        archivo1 = open (funcionArchivo, "rt")
        print ("Ya existe")
        print (len(archivo1.readlines()))
        archivo1.close()
    except IOError:
        print ("Se produjo un error")
        
#funcionArchivo = "C:\\pythonjimenez\\Archivos\\funcionPrueba.txt"
funcionArchivo = "C:\\clon\\pythonjimenez\\ArchivosPython\\Archivo2\\funcionPrueba.txt"
ValidaciondeArchivo (funcionArchivo)