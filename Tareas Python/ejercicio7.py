#Encontrar un número natural n más pequeño tal que la suma de los n primeros números naturales (1 + 2 + 3 + 4.....) exceda de una cantidad (máximo) introducida por el teclado. Es decir cuantos números de la serie de los naturales debo sumar para superar el dato máximo.

max= int(input("Ingrese un numero maximo: "))
sum= 0
n = 0

while sum <= max:
    n += 1
    sum += n

print(f'Se necesitan sumar los primeros {n} números naturales para superar el valor máximo introducido:')

