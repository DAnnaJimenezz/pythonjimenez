factorial = 1
sumatoria = 0

for i in range(1, 21):
    factorial *= i
    sumatoria += factorial
    print(f"{i}! = {factorial}")
    
print(f"\nLa sumatoria de factoriales del 1 al 20 es: {sumatoria}")
