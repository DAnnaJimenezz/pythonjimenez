import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contratosPSN"
)

class Candidato():
    def __init__(self, tipoDocumento, numDocumento, nombre, email, telefono):
        self.__tipoDocumento = tipoDocumento
        self.__numDocumento = numDocumento
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono

    def getTipoDocumento(self):
        return self.__tipoDocumento

    def getNumDocumento(self):
        return self.__numDocumento

    def getNombre(self):
        return self.__nombre

    def getEmail(self):
        return self.__email

    def getTelefono(self):
        return self.__telefono

    def getDatos(self):
        return self.getTipoDocumento(), self.getNumDocumento(), self.getNombre(), self.getEmail(), self.getTelefono()
    
    def agregarCandidato():
        tipoDocumento = input("Ingrese su tipo de documento:")
        numDocumento = int(input("Ingrese su numero de documento:"))
        nombre = input("Ingrese su nombre:")
        email = input("Ingrese su correo electronico:")
        telefono = (input("Ingrese su numero de telefono:"))

        insertar = "INSERT INTO candidato (tipoDocumento, numDocumento, nombre, email, telefono) VALUES (%s, %s, %s, %s, %s)"
        valores = (tipoDocumento, numDocumento, nombre, email, telefono)

        cursor = db.cursor()
        cursor.execute(insertar, valores)
        db.commit()
        cursor.close()

    
    def consultarDatos():
        campo = input('Ingrese el campo a consultar:')
        consulta = f"SELECT {campo} FROM candidato;"
        print(consulta)

        cursor = db.cursor()
        cursor.execute(consulta)
        for dato in cursor:
            print(dato)
        cursor.close()


    def agregarCampo():
        campo = input('Ingrese el nombre del nuevo campo:')
        tipoDato = input('Ingrese el tipo de dato y el limite de caracteres del campo:')
        agrCampo = f"ALTER TABLE candidato ADD COLUMN {campo} {tipoDato};"
        print(agrCampo)

        cursor = db.cursor()
        cursor.execute(agrCampo)
        db.commit()
        cursor.close()


    def eliminarDatos():
        campo = input('Ingrese el campo a consultar:')
        dato = input('Ingrese el dato a eliminar:')
        eliminar = f"DELETE FROM candidato WHERE {campo} = %s;"
        print(eliminar)

        cursor = db.cursor()
        cursor.execute(eliminar, (dato,))
        db.commit()
        cursor.close()

    
    def modificarRegistro():
        campo1 = input('Ingrese el nombre del campo actual:')
        dato1 = input('Ingrese el dato nuevo del campo que eligió:')
        campo2 = input('Ingrese un campo relacionado con el dato a cambiar:')
        dato2 = input('Ingrese el dato del campo relacionado que eligió:')
        
        mfcarRegistro = f"UPDATE candidato SET {campo1} = %s WHERE {campo2} = %s;"
        print(mfcarRegistro)

        cursor = db.cursor()
        cursor.execute(mfcarRegistro, (dato1, dato2))
        db.commit()
        cursor.close()