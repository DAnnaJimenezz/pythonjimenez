# Leer los dos números desde el teclado
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Determinar si los dos números son iguales
son_iguales = numero1 == numero2

# Determinar si los dos números son diferentes
son_diferentes = numero1 != numero2

# Determinar si el primero es mayor que el segundo
es_mayor = numero1 > numero2

# Determinar si el segundo es mayor o igual que el primero
es_mayor_o_igual = numero2 >= numero1

# Mostrar los resultados
print("Los dos números son iguales:", son_iguales)
print("Los dos números son diferentes:", son_diferentes)
print("El primer número es mayor que el segundo:", es_mayor)
print("El segundo número es mayor o igual que el primero:", es_mayor_o_igual)
