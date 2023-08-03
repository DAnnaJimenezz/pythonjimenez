from Empresa import *
import csv
empresa =[]
with open('C:\\clon\\pythonjimenez\\ClasesTarea\\Contratos_de_concesi_n_de_juegos_de_suerte_y_azar.csv', 'r', encoding= 'utf-8') as csvArchivo:
    csvLectura=csv.reader(csvArchivo)
    for row in csvLectura:
        objeto=Empresa(row[0],row[1],row[2],row[5])
        print(objeto.getDatos())
        empresa.append(objeto)

    def sumaLista(empresa):
        sum = 0
        sum=0
        for empresa in row[1]:
            sum+=empresa
        return sum
    
    def promedioLista (empresa):
        return sumaLista(empresa)/len(row[1])
    
    def mayorLista(empresa):
        mayor=0
        for empresa in row[1]:
            if empresa > mayor:
                mayor = empresa
        return mayor
    
    def menorLista(empresa):
        menor=10000
        for empresa in row[1]:
            if empresa < menor:
                menor = empresa
        return menor
    
    def modaLista(empresa):
        cont=0
        rep=0
        for empresa in row[1]:
            for i in row[1]:
                if modaLista == i:
                    cont+=1
                if cont > rep:
                    modaLista= i
        return modaLista
    
    def medianaLista(empresa):
        mediana=(len(row[1]))
        if mediana % 2==0:
            medianaLista = (row[1][mediana//2-1]+row[0][mediana//2])/2
        else:
            medianaLista=row[1][mediana//2]
        return medianaLista
    
    with open ('C:\\clon\\pythonjimenez\\ClasesTarea\\Resultados.txt', 'w', encoding= 'utf-8') as archivoFinal:
        for obj in empresa:
                print("NIT:', {obj.getNIT()}\n")
                print("contrato: , {obj.getContrato()}\n")
                print("nombreOperador: , {obj.getNombreOperador()}\n")
                print("modalidadJuego: , {obj.getModalidadJuego()}\n")
            
                respuestas = obj.getDatos()
                archivoFinal.write("La suma de la lista es: {sumaLista(respuestas)}\n")
                archivoFinal.write("El promedio de la lista es: {promedioLista(respuestas)}\n")
                archivoFinal.write("El número mayor de la lista es: {mayorLista(respuestas)}\n")
                archivoFinal.write("El número menor de la lista es: {menorLista(respuestas)}\n")
                archivoFinal.write("La moda de la lista es: {modaLista(respuestas)}\n")
                archivoFinal.write("La mediana de la lista es: {medianaLista(respuestas)}\n")