import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

lista=llenarLista(10,15)
print(lista)

n=(int(input("Ingrese un numero:")))

def numeroLista(lista):
    num=0
    while n not in lista:
        lista.append(num)
        n=(int(input("Ingrese un numero:")))
    return numeroLista

n=(int(input("Ingrese un numero:")))

print(lista)



