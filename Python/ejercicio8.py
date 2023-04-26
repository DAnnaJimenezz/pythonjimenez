# Ingrese los nombres de dos personas
nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")

# Verificar si hay coincidencia
if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("Coincidencia")
else:
    print("No hay coincidencia")
