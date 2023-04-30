#Determinar los divisores de un número introducido por teclado

num=int(input("Ingrese un número: "))

for i in range (1,num+1):
    if num % i ==0:
        print (i)