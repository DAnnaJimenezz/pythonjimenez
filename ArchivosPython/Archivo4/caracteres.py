import os 
caracteres = {chr(ch): 0 for ch in range(256)}
#funcionArchivo = input("Ingresa el nombre del archivo a analizar:")
def conteoDeCaracteres (funcionArchivo):
    try:
        archivo = open (funcionArchivo, "rt")
        for line in archivo:
            for char in line:
                if char.isalpha():
                    caracteres[char] += 1 
        archivo.close()
        for char in caracteres.keys():
            c = caracteres [char]
            if c > 0:
                print (char, '->', c)
    except IOError:
        print ("Se produjo un error")
funcionArchivo = "C:\\clon\\pythonjimenez\\ArchivosPython\\Archivo4\\caracteresArchivo.txt"
conteoDeCaracteres (funcionArchivo)