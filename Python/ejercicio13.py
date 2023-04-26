numero = 0
suma = 0

while numero != -1:
    numero = int(input("Ingrese un número (-1 para terminar): "))
    if numero != -1:
        suma += numero

print("La suma de los números ingresados es:", suma)
