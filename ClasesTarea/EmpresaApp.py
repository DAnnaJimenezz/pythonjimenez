from Empresa import *
import csv
empresa =[]
with open('C:\\Users\\Camila Castro\\Downloads\\Contratos_de_concesi_n_de_juegos_de_suerte_y_azar.csv', 'r', encoding= 'utf-8') as csvArchivo:
    csvLectura=csv.reader(csvArchivo)
    for row in csvLectura:
        objeto=Empresa(row[1],row[0],row[2],row[5])
        print(objeto.getDatos())
        empresa.append(objeto)