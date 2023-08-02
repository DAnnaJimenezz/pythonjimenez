try:
    stream = open ('C:\\pythonjimenez\\ArchivosPython\\Archivo6\\himno.txt', 'r')
    cont = 1
    linea = stream.readline()
    c=1
    while linea != "":
        print (f"{c} {linea}")
        linea = stream.readline()
        c+=1
    stream.close()
except IOError:
    print ("Ocurrio un error")