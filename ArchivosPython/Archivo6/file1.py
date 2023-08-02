try:
    stream = open ('C:\\pythonjimenez\\ArchivosPython\\Archivo6\\himno.txt', 'r')
    for linea in stream.readlines():
        print (linea)
    stream.close()
except IOError:
    print ("Ocurrio un error")