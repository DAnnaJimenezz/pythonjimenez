import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(l1):
    sum1=0
    for x in l1:
        sum1+=x
    return sum1

def mayorLista(l1):
    mayor=0
    for x in l1:
        if x > mayor:
            mayor = x
    return mayor

def menorLista(l1):
    menor=10000
    for x in l1:
        if x < menor:
            menor = x
    return menor 

def promedioLista(l1):
    promedio=0
    promedio = sumaLista(l1) /len(l1)
    return promedio

def cantidadLista(l1):
    pares1=0
    impares1=0
    for x in l1:
        if x % 2 == 0:
            pares1 += 1
        else:
            impares1 += 1
    return pares1, impares1

l1=llenarLista(10,20)
print(l1)

print("La suma de la lista es:", sumaLista(l1))
print("El numero mayor de la lista es:", mayorLista(l1))
print("El numero menor de la lista es:", menorLista(l1))
print("El promedio de la lista1 es:", promedioLista(l1))
print("El numero de pares es: ", cantidadLista(l1))
print("El numero de cantidad de impares es:", cantidadLista (l1))

print()
    

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista2(l2):
    sum2=0
    for j in l2:
        sum2+=j
    return sum2

def mayorLista2(l2):
    mayor=0
    for j in l1:
        if j > mayor:
            mayor = j
    return mayor

def menorLista2(l2):
    menor=10000
    for j in l1:
        if j < menor:
            menor = j
    return menor 

def promedioLista2(l2):
    promedio=0
    promedio = sumaLista2(l2) /len(l2)
    return promedio

def cantidadLista2(l1):
    pares1=0
    impares1=0
    for x in l1:
        if x % 2 == 0:
            pares1 += 1
        else:
            impares1 += 1
    return pares1, impares1


l2=llenarLista(10,20)
print(l2)

print("La suma de la lista es:", sumaLista(l2))
print("El numero mayor de la lista es:", mayorLista(l2))
print("El numero menor de la lista es:", menorLista(l2))
print("El promedio de la lista2 es: ", (promedioLista2 (l2)))
print("El numero de pares es: ", cantidadLista2(l2))
print("El numero de cantidad de impares es:", cantidadLista2 (l2))


print()

def promedioConjunto():
    promedio= (sumaLista (l1) + sumaLista2 (l2))/2
    return promedio

def cantidadPares ():
    
#Falta: Cantidad de pares, impares, suma mayor de la listas.
