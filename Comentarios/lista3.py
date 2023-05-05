import random    
lista=[]
cuadrado=[]
tam=random.randint(5,10)    #Utiliza random para que el mismo de numeros aleatorios, uyiliza random.randint para declarar un inicio y un final para dar numeros aleatorios 
print(tam)
for i in range(tam):
    num=random.randrange(100)  #Utiliza random.randrange para determinar un limite 
    lista.append(num)  #Utiliza lista.append para añadir un elemento al final de la lista
print(lista)

for i in range(len(lista)):
    cuadrado.append(lista[i]**2)
    #lista[i]=lista[i]**2             #Con cualquiera de las siguientes se eleva a la potencia elementos de una lista
    # print(lista[i]*lista[i])  
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado)
print(sum(lista))