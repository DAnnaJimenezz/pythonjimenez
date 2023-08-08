from Candidato import *

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contratosPSN"
)

while True:
    print('MENU PRINCIPAL')
    print('1- Candidato')
    print('2- Salir')
    opcion = int(input('Elija que funciones desea realizar:'))

    if opcion == 1:
        print ()
        print('MENU CANDIDATO')
        print('1- Registrar Candidato')
        print('2- Consultar Candidato')
        print('3- Eliminar Candidato')
        print('4- Agregar Campo Nuevo')
        print('5- Modificar Registro')
        print('0- Cerrar Programa')
        opcionN1 = int(input('Elija que funciones desea realizar:'))    
    elif opcion == 2:
        print('Bye Bye!!')
        break

    if opcionN1==0:
        print('Bye Bye!!')
        break

    elif opcionN1 == 1:
        Candidato.agregarCandidato()
        print('REGISTRO EXITOSO!!')

    elif opcionN1 == 2:
        print('ESCRIBA ALGUNAS DE ESTAS OPCIONES:')
        print()
        print("1 - tipoDocumento")
        print("2 - numDocumento")
        print("3 - nombre")
        print("4 - email")
        print("5 - telefono")
        Candidato.consultarDatos()
        print('CONSULTA EXITOSA!!')

    elif opcionN1 == 3:
        print('ESCRIBA EL DATO QUE QUIERE ELMINAR:')
        Candidato.eliminarDatos()

    elif opcionN1 == 4:
        print('USTED VA A CREAR UN NUEVO CAMPO:')
        Candidato.agregarCampo()
        print('CAMPO AGREGADO EXITOSAMENTE!!')

    elif opcionN1 == 5:
        print('USTED VA A MODIFICAR UN REGISTRO:')
        Candidato.modificarRegistro()
        print('REGISTRO MODIFICADO EXITOSAMENTE!!')

    else:
        print('Ingrese una opcion valida')