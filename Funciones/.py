import random

def llenado(tami,tamf,rangoi,rangof):
    lista=[]
    lista=[random.randint(rangoi,rangof) for i in range(tami,tamf)]
    return lista

l1=llenado(50,100,100,500)

print(l1)

def Ascendente(lista):
    for j in range(len(lista)):
        for g in range(j +1, len(lista)):
            if lista[j] >  lista[g]:
                aux=lista[j]
                lista[j]=lista[g]
                lista[g]=aux
    return f"la lista ordenada en orden ascendente: {lista}"
listaascedente=(Ascendente(l1))
print(listaascedente)

def cuartiles (l1):
    listaOrdenada = Ascendente (l1)
    x = len(listaOrdenada)
    c1 = listaOrdenada [int(x * 0.25)]
    c2 = listaOrdenada [int(x * 0.5)]
    c3 = listaOrdenada [int(x * 0.75)]
    
    return c1,c2,c3

print(cuartiles(l1))

def quintiles (l1):
    listaOrdenada = Ascendente (l1)
    x = len(listaOrdenada)
    q1 = listaOrdenada [int(x * 0.2)]
    q2 = listaOrdenada [int(x * 0.4)]
    q3 = listaOrdenada [int(x * 0.6)]
    q4 = listaOrdenada [int(x * 0.8)]

    return q1,q2,q3,q4

print(quintiles(l1))




    
    
