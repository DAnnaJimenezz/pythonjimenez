# x = int(input("Ingrese un numero:"))
# while x < 10:
#     x = int(input("Ingrese otro numero:"))

# op = x / 0
# print (op)
# -------------------------------------------
x = int(input("Ingrese un numero:"))        

while x < 10:
    try:
        x = int(input("Ingrese un numero nuevamente:"))        
        op = x / 0
        print (op)
    
    except ZeroDivisionError:
        print ("No se puede dividir por cero")
print ("El programa a terminado")