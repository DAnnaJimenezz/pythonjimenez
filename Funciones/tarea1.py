import random

def llenado(tami,tamf,rangoi,rangof):
    lista=[]
    lista=[random.randint(rangoi,rangof) for i in range(tami,tamf)]
    return lista

listado=llenado(50,100,100,500)

print(listado)

def Ascendente(lista):
    for j in range(len(lista)):
        for g in range(j +1, len(lista)):
            if lista[j] >  lista[g]:
                aux=lista[j]
                lista[j]=lista[g]
                lista[g]=aux
    return f"la lista ordenada en orden ascendente: {lista}"

print(Ascendente(listado))

def cuartil(lista):
    formula=0
    n = len(lista)
    listaCuartil=[]
    formula2=0
    for k in range(1, 4):
        if len(lista) % 2!=0:
            formula=(k*(n+1)) / 4
            formula2=round(formula)
            posicion=lista[formula2-1]
            print(f"Q{k} = posicion {formula} valor en lista {posicion}")
            listaCuartil.append(formula)
            print(listaCuartil)
            
        else:
            formula = (k*n)/4
            conv=round(formula)
            posicion= lista[formula2]
            print(f"Q{k} = {formula} en lista {posicion}")
            listaCuartil.append(formula)
            print(listaCuartil)
print(cuartil(listado))


def quintil(lista):
    formula=0
    tamaño = len(lista)
    listaCuartil=[]
    formula2=0
    for b in range(1, 5):
        if len(lista) % 2!=0:  
            formula=(b*(tamaño+1)) / 5
            formula2=round(formula)
            pos=lista[formula2-1]
            print(f"k{b} = posicion {formula} valor en lista {pos}")
            listaCuartil.append(formula)
            print(listaCuartil)
        else:
            formula = (b*tamaño)/5
            conv=round(formula)
            print(f"k{b} = {formula}")
            listaCuartil.append(formula)
            print(listaCuartil)

print(quintil(listado))