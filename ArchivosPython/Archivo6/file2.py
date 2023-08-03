counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
cont = 0
try:
    stream = open ('C:\\clon\\pythonjimenez\\ArchivosPython\\Archivo6\\himno.txt', 'r', encoding= 'utf-8')
    for linea in stream:
        for chr in linea:
            if chr.isalpha():
                counters[chr.lower()] += 1
                cont +=1
    stream.close()

    with open ('C:\\clon\\pythonjimenez\\ArchivosPython\\Archivo6\\himno2.txt', 'w', encoding = 'utf-8') as archivoFinal:
        for char, cont in counters.items():
            archivoFinal.write(f'El total de letras en el himno de soacha es: {cont}\n')
    print ("El conteo final fue guardado exitosamente en el archivo himno2.txt")

except IOError:
    print ("Algo salio mal")