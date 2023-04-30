#Calcular el máximo de números positivos introducidos por teclado, sabiendo que metemos números hasta que introduzcamos uno negativo. El negativo no cuenta.

max= 0
while True:
    numero = int(input("Introduce el numero positivo que desees: "))
    if numero < 0:
        break
    if numero > max:
        max = numero

print("El numero mayor ingresado es:", max)
