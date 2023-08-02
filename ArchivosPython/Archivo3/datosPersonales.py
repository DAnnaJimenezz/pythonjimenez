import os 
def DatosPerosnales (funcionArchivo, datos):
    try:
        archivo = open(funcionArchivo, "a")
        for i in datos:
            archivo.write(i + '\n')
        archivo.close()
        print ("Los datos fueron agregados correctamente")
    except IOError:
        print ("Se produjo un error")

nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
genero = input("Ingrese su genero:")
edad = input("Ingrese su edad:")
email = input("Ingrese su correo electronico:")
deporteFavorito = input("Ingrese su deporte favorito:")
generoDeMusica = input("Ingrese su genero favorito de musica:")
datos = (nombre, apellido, genero, edad, email, deporteFavorito, generoDeMusica)

funcionArchivo = "C:\\clon\\pythonjimenez\\ArchivosPython\\Archivo3\\daticosPersonales.txt"
DatosPerosnales (funcionArchivo, datos)