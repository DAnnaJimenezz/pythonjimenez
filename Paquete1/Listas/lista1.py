import random

def FunA (tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=FunA (10,15)
print(l1)