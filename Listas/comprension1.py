import math
import random
raiz=2

tam=random.randint(5,10)
lista= [random.randrange (100) for i in range (tam)]
lista2=[j for j in lista]
print(lista)

par=[0 for j in lista if j%2==0]
print(par)

raiz=[j for j in lista if math.sqrt(raiz/lista)]
print(raiz/lista)


