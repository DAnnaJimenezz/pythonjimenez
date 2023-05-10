import random
lista=[]
lista2=[]
cont=0
sum1=0
sum2=0
mayor=0
menor=10000
promedio1=0
promedio2=0
pares1=0
pares2=0
impares1=0
impares2=0

n = random.randint (10,20)
print (n)

for n in range (n):
    num=random.randrange (25)
    lista.append (num)
print (lista )

for n in lista:
    sum1 = sum1 + n
    cont+=1
    if n % 2 == 0:
        pares1 += 1
    else:
        impares1 += 1
   
print (f'La suma de la lista es: {sum1}')

for n in lista:
    if n > mayor: 
        mayor = n
    if n < menor:
        menor = n

promedio1=sum1/len(lista)

print (f'El numero mayor de la lista es: {mayor}')
print (f'El numero menor de la lista es: {menor}')
print(f'El promedio de la lista es: {promedio1}')

if n % 2 == 0:
    print (f'Cantidad de numeros pares: {n}')
else:
    print (f'Cantidad de numeros impares: {n}')

j = random.randint (20,30)
print (j)

for j in range (n):
    num=random.randrange (35)
    lista2.append (num)
print (len(lista2))
print (lista2)

for j in lista2:
    sum2 = sum2 + j
    cont+=1
    if j % 2 == 0:
        pares2 += 1
    else:
        impares2 += 1

print (f'La suma de la lista 2 es: {sum2}')

if sum1 > sum2:
    print (f'La suma mayor entre las dos es lista: {sum1}')
else:
    print (f'La suma mayor entre las dos es lista 2: {sum2}')
j
for j in lista2:
    if j > mayor: 
        mayor = j
    if j < menor:
        menor = j

promedio2=sum2/len(lista2)

print (f'El numero mayor de la lista 2 es: {mayor}')
print (f'El numero menor de la lista 2 es: {menor}')
print (f'El promedio de la lista 2 es: {promedio2}')

promedioConjunto = (promedio1 + promedio2)/2
print (f'El promedio conjunto es: {promedioConjunto}')

if pares1 < pares2:
    print (f'La lista 2 tiene mas pares que la lista: {pares2}')
else: 
    print (f'La lista tiene mas pares que la lista 2: {pares1}')

if impares1 < impares2:
    print (f'La lista 2 tiene mas impares que la lista: {impares2}')
else: 
    print (f'La lista tiene mas impares que la lista 2: {impares1}')