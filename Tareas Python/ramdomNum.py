#Genere un número aleatorio y pida al usuario que lo adivine

import random
num= random.randint(1, 10)

adivina= int(input("Adivina un numero entre 1 y 10:"))

while adivina != num:
    if adivina < num:
        print ("El numero es menor, Intenta de nuevo:")
    else:
        print ("El numero es mayor, Intenta de nuevo: ")
    adivina= int(input("Adivina un numero entre 1 y 10: "))

print ("Ese es el numero correcto")