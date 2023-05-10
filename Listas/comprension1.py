import math
import random
raiz=[]

tam=random.randint(5,10)
lista= [random.randrange (100) for i in range (tam)]
print(lista)

par=[j for j in lista if j%2==0]
print(par)

raiz= [num ** 0.5 for num in lista]
print (raiz)
 
