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
    cuartil1=[]
    cuartil2=[]
    formula=0
    n = len(lista)
    listaCuartil=[]
    formula2=0
    for k in range(1, 4):
        pos2=formula2
        formula=(k*(n+1)) / 4
        formula2=round(formula)
        posicion=lista[formula2-1]
        print(f"Q{k} = posicion {formula} valor en lista {posicion}")
        listaCuartil.append(formula)
        print(listaCuartil)
        if k == 1:
            cuartil1=lista[:formula2]
            print(cuartil1)                
        elif k == 2:
            cuartil2=lista[pos2:formula2]
            print(cuartil1) 
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
l1=(listado)
print(quintil(listado))

def cuartillista(lista,numero):
    total=[]
    while numero>4:
        numero=int(input("ingrese el nunero del cuartil que desea saber"))
    cuartil=round(numero*(len(lista)+1)/4),3
    total.append (cuartil)
    return total
    
def quintillista(lista,numero):
    total=[]
    while numero>5:
        numero=int(input("ingrese el nunero del quintil que desea saber"))
    cuartil=round(numero*(len(lista)+1)/5),3
    total.append (quintil)
    return total

#print(cuartillista(l1,n))
numero=int(input("ingrese el nunero del cuartil que desea saber"))
print("el cuantil es:",cuartillista(l1,numero))

