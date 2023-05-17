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

def paresLista (l1):
    par = 0
    for x in l1:
        if x % 2 == 0:
            par += 1
    return par

def imparLista (l1):
    impar = 0
    for x in l1:
        if x % 2 == 0:
            impar += 1
    return impar

l1=llenarLista(10,20)
print(l1)

print("La suma de la lista es:", sumaLista(l1))
print("El numero mayor de la lista es:", mayorLista(l1))
print("El numero menor de la lista es:", menorLista(l1))
print("El promedio de la lista1 es:", promedioLista(l1))
print(f'La lista2 tiene esta cantidad de pares: {paresLista (l1)}')
print(f'La lista2 tiene esta cantidad de impares: {imparLista (l1)}')

print()
print()
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

def paresLista2(l2):
    par = 0
    for j in l2:
        if j % 2 == 1:
            par += 1
    return par

def imaparesLista2 (l2):
    impar = 0
    for j in l2:
        if j % 2 == 1:
            impar += 1
    return impar 


l2=llenarLista(10,20)
print(l2)

print("La suma de la lista es:", sumaLista(l2))
print("El numero mayor de la lista es:", mayorLista(l2))
print("El numero menor de la lista es:", menorLista(l2))
print("El promedio de la lista2 es: ", (promedioLista2 (l2)))
print(f'La lista2 tiene esta cantidad de pares:{paresLista2 (l2)}')
print(f'La lista2 tiene esta cantidad de impares:{imaparesLista2 (l2)}')


print()
print()
print()

def promedioConjunto():
    promedio= (sumaLista (l1) + sumaLista2 (l2))/2
    return promedio
print ("El promedio de las dos listas es:", promedioConjunto ())

def cantidadPares ():
    mayorPares = 0
    if paresLista (l1) > paresLista2 (l2):
        mayorPares = paresLista (l1)
    else:
        mayorPares = paresLista2 (l2)
    return mayorPares

print (f'La lista con mas cantidad de pares es: {cantidadPares()}')


def cantidadImpares ():
    mayorImpares = 0 
    if paresLista (l1) < imaparesLista2 (l2):
        mayorImpares = paresLista (l1)
    else:
        mayorImpares = imaparesLista2 (l2)
    return mayorImpares

print (f'La lista con mas cantidad de impares es: {cantidadImpares()}')


def sumaMayor (l1, l2):
    sum1 = sum (l1)
    sum2 = sum (l2)
    if sum1 > sum2:
        return sum2
    elif sum1 < sum2:
        return sum2
    else:
        return "La suma es igual"
    
print("La suma mayor entre las dos listas es:", sumaMayor (l1, l2))