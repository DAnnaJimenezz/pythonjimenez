import random

cont=0
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
sum1=0
sum2=0

lista = random.randrange(20, 30)
lista = [round(random.random()*5,2)for j in range(lista)]
print(lista)
nota=["aprobado" if j > 3 else "desaprobado" for j in lista]

a1=lista[:5]
a2=nota[:5]
print(a1)
print(a2)

a3=lista[5:]
a4=nota[5:]
print(a3)
print(a4)

print("Aprobados")
aprobado=[j for j in lista if j>3] 
print(aprobado)
a5=lista[:5]
a6=aprobado[:5]
print()

print("Desaprobados")
desaprobado=[j for j in lista if j < 3]
print(desaprobado)
a7=lista[5:]
a8=aprobado[5:]
print()

lista.sort()
print(lista)

print("0 a 1")
uni1=[j for j in lista if j < 2]
print(uni1)

print("1 a 2")
uni2=[j for j in lista if j > 1 and j < 3]
print(uni2)

print("2 a 3")
uni3=[j for j in lista if j > 2 and j < 4]
print(uni3)

print("3 a 4")
uni4=[j for j in lista if j > 3 and j <=5]
print(uni4)

print("Suma Aprobados")
aprobo=[sum(aprobado)]
print(aprobo)

print("Suma Desaprobados")
desaprobo=[sum(desaprobado)]
print(desaprobo)

promApro=[sum(aprobo) / len(aprobado)]
promDesa=[sum(desaprobo) / len(desaprobado)]
print(f'El promedio de aprobados es: {promApro}')
print(f'El promedio de desaprobados es: {promDesa}')