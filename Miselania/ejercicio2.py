#Llenar un arreglo de n elementos con números generados con la función random. No puede haber números repetidos. Si intenta ingresar al arreglo un número que ya existe, imprimirlo para anunciar que ese número ya está en el arreglo.
import random
n=[]
lista=[]

num= random.randint(15, 25)
print(num)

for i in range(num):
    num=random.randrange(100)
    lista.append(num)
print(lista)

n=(int(input("Ingrese un numero:")))

while n not in lista:
     lista.append(num)
     n=(int(input("Ingrese un numero:")))

print(lista)
