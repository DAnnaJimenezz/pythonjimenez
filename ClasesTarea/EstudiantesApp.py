from Estudiante import *
import csv
estudiante =[]
with open('C:\\Users\\APRENDIZ SENA\\Downloads\\Saber_11__2019-2.csv') as csvArchivo:
    csvLectura=csv.reader(csvArchivo)
    for row in csvLectura:
        objeto=Estudiante(row[38],row[40],row[64],row[62])
        print(objeto.verDatos())
        estudiante.append(objeto)
        
for estu in estudiante:
    print(estu.getNombre())