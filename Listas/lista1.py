import random 
lista =[]
sum=0
cont=0
mayor=0
menor=100000 

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

print(f"La suma es: {sum}")
print(f"El promedio es: {sum/cont}")
print (f'El numero mayor es: {mayor}')
print (f'El numero menor es: {menor}')