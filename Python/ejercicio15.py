numero = input("Ingrese un número entero: ")
suma_digitos = 0

for digito in numero:
    suma_digitos += int(digito)

print("La suma de los dígitos de", numero, "es:", suma_digitos)
