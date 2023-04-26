# Ingrese un día de la semana
dia = input("Ingrese un día de la semana: ")

# Imprimir un mensaje diferente según el día ingresado
if dia.lower() == "lunes":
    print("¡Feliz lunes!")
elif dia.lower() == "viernes":
    print("¡Feliz viernes!")
elif dia.lower() == "sábado" or dia.lower() == "domingo":
    print("¡Buen fin de semana!")
else:
    print("Ese día no está en la lista.")
