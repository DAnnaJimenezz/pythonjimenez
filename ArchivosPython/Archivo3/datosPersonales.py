import os 
def ValidaciondeArchivo (funcionArchivo):
    try:
        nombre = input("Ingrese su nombre:")
        apellido = input("Ingrese su apellido:")
        edad = int(input("Ingrese su edad:"))
        email = input("Ingrese su correo electronico:")
        with open (funcionArchivo,"w+") as daticosPersonales:
            print ("Datos personales agregados correctamente")
        daticosPersonales.close()
    except IOError:
        print ("Se produjo un error")
        
#funcionArchivo = "C:\\pythonjimenez\\Archivos\\funcionPrueba.txt"
funcionArchivo = "C:\\clon\\pythonjimenez\\ArchivosPython\\Archivo3\\daticosPersonales.txt"
ValidaciondeArchivo (funcionArchivo)