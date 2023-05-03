inicio= int(input("Ingrese el inicio: "))
final= int(input("Ingrese el final:"))
incrementar= int(input("Ingrese valor para incrementar:"))
decrementar= int(input("Ingrese valor para decrementar:"))


for i in range (inicio , final +1, incrementar):
    print (i)

for i in range (inicio , final -1, -decrementar):
    print (i)

n=int(input("Ingrese un numero positivo :"))

for i in range (inicio, final,incrementar ):
    
    if i % n == 0:
        print(i,"Es multiplo de",n)
   
    else: 
        print(i)  