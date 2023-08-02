counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
cont = 0
try:
    stream = open ('C:\\pythonjimenez\\ArchivosPython\\Archivo6\\himno.txt', 'r', encoding= 'utf-8')
    for linea in stream:
        for chr in linea:
            if chr.isalpha():
                counters[chr.lower()] += 1
                cont +=1
    print (f'La linea {linea} tiene los siguientes caracteres {cont}' ) 

    stream.close()
except IOError:
    print ("Algo salio mal")
