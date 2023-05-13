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
    menor=10000
    for i in lista:
        if i < menor:
            menor = i
    return menor

def modaLista(lista):
    cont=0
    rep=0
    for modaLista in lista:
        for i in lista:
            if modaLista == i:
                cont+=1
            if cont > rep:
                modaLista= i
    return modaLista

def ascendenteLista(lista):
    aux=0
    for i in range(len(lista)):
        for n in range (i+1,len(lista)):
            if lista[i]>lista[n]:
                aux=lista[i]
                lista[i]=lista[n]
                lista[n]=aux
    return lista

def descendenteLista(lista):
    aux=0
    for i in range(len(lista)):
        for n in range (i+ 1,len(lista)):
            if lista[i]<lista[n]:
                aux=lista[i]
                lista[i]=lista[n]
                lista[n]=aux
    return lista
   
def medianaLista(lista):
    mediana=(len(lista))
    if mediana % 2==0:
        medianaLista = (lista[mediana//2-1]+lista[mediana//2])/2
    else:
        medianaLista=lista[mediana//2]
    return medianaLista

l1=llenarLista(10,15)
print(l1)

print("La suma de la lista es:", sumaLista(l1))

print("El promedio de la lista es: ", promedioLista(l1))

print("El número mayor de la lista es:" , mayorLista(l1))

print("El número menor de la lista es: " ,menorLista(l1))

print("La moda de la lista es: ", modaLista(l1))

print("Forma ascendente: ", ascendenteLista(l1))

print("La forma descendente: ", descendenteLista(l1))

print("La mediana de la lista es: ", medianaLista(l1))
