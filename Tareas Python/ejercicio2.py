#Determinar si un numero es o no es primo

num=int(input("Ingresa un número: "))
num2=1
num3=0
while num2 <= num:
    if num % num2 == 0:
        num3=num3+1
    num2=num2+1
if num3==2:
    print("El número",num,"Es primo")
else:
    print("El número", num, "No es primo")