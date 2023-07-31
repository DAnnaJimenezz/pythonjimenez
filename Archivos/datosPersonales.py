import os 
def ValidaciondeArchivo (datosPersonales):
    try:
        archivo = open (datosPersonales, "r+t")
        nombre = input("Ingrese su nombre:")
        apellido = input("Ingrese su apellido:")
        edad = input("Ingrese su edad:")
        email = input("Ingrese su correo electronico")
        miPersona = (nombre, apellido, edad, email)
        
        archivo.close()
    except IOError:
        print ("Se produjo un error")
        
funcionArchivo = "C:\\pythonjimenez\\Archivos\\funcionPrueba.txt"
ValidaciondeArchivo (funcionArchivo)