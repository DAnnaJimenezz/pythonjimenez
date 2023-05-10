import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def mayorLista(lista):
    for i in lista:
        if i > lista:
            mayorLista = i
    return mayorLista
        
def menorLista(lista):
    for i in lista:
        if i < lista:
            menorLista = i
    return menorLista
        
l1=llenarLista(35,50)
print(l1)

print(sumaLista(l1))

print(promedioLista(l1))

print(mayorLista(l1))

print(menorLista(l1))

