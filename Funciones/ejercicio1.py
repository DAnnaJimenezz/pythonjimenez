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
    if l1 > lista:
        mayorLista = l1
    if l2 > lista:
        mayorLista = l2
    if l3 > lista:
        mayorLista = l3
        
def menorLista(lista):
    if l1 < lista:
        menorLista = l1
    if l2 < lista:
        menorLista = l2
    if l3 < lista:
        menorLista = l3

        
l1=llenarLista(20,35)
l2=llenarLista(10,60)
l3=llenarLista(0,100)
print(l1)
print(l2)
print(l3)

print(sumaLista(l1))
print(sumaLista(l2))
print(sumaLista(l3))

print(promedioLista(l1))
print(promedioLista(l2))
print(promedioLista(l3))

print(mayorLista(l1))
print(mayorLista(l2))
print(mayorLista(l3))

print(menorLista(l1))
print(menorLista(l2))
print(menorLista(l3))
