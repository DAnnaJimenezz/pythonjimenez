x=0
y=0
cont=0
while not (x>y or y>x):
    x= int(input("Ingrese un numero:"))
    y= int(input("Ingrese un numero:"))
if x < y:
    print (f'El numero menor es: {x}')
else: 
    print (f'El numero mayor es: {x}')

if y > x:
    print (f'El numero mayor es: {y}')
else: 
    print (f'El numero menor es: {y}')

if (x >= y):
    
    print (f'La resta entre los dos numeros es: {x or y}')
    
else:
    print(f'El resultado de la resta es: {x - y} ')

if (x > y):
    print ("Se puede seguir restando")

    z=int(input("Ingrese nuevamente un numero: "))
    cont=cont-z
    print(f'El resultado es:{cont}')

else: 
    print("No se puede seguir restando.")


    