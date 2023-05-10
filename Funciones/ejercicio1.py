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
    mayor=0
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor
        
def menorLista(lista):
    menor=0
    for i in lista:
        if i < menor:
            menor = i
    return menor
        
l1=llenarLista(5,10)
print(l1)

print(sumaLista(l1))

print(promedioLista(l1))

print(mayorLista(l1))

print(menorLista(l1))

