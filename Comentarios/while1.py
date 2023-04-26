
# num=1
# print(type(num))
# num="sena"
# print(type(num))
num=1
cont=0
sum=0
menor=1000000
mayor=0
while num!=0:    #Usa el ciclo while 
    num=int(input('ingrese numero'))
    cont=cont+1   #La variable cont es igual a la misma variable y le suma 1 por cada iteracion del bucle 
    sum=sum+num   #La variable suma es igual a la misma variable y le suma num que es igual a 1 
    if num>mayor:  #La condicion if declara 1 sea mayor que 1000000
        mayor=num
    if num<menor and num!=0:  #La condicion if declara si 1 es menor a 100000 y and agrega otra condicion de que num no sea igual a cero
        menor=num

print(f'fueron ingresados {cont-1} numeros')
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)}')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')