import math
import random 
lista =[]
sum=0
cont=0
mayor=0
menor=100000 
moda= 0
media=0
resta=0
cuadrado=2
division= 0

tam = random.randint (10,20)
print (tam)

for i in range (tam):
    num=random.randrange (100)
    lista.append (num)
print (lista )

for i in lista:
    sum+=i
    cont+=1
    if i > mayor:
        mayor= i
    if i < menor:
        menor = i
    if i in lista:
        sum/cont

for i in lista:
    i = resta - (sum/cont)
    cuadrado = resta ** 2
    sum += cuadrado 
    division = sum/cont 
raiz = math.sqrt(division)

print(f"La suma es: {sum}")
print(f"El promedio es: {sum/cont}")
print (f'El numero mayor es: {mayor}')
print (f'El numero menor es: {menor}')
print (f'La media es: {sum/cont}')
print (f'La desviacion estandar es: {raiz}')

