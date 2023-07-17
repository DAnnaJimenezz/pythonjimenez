import math
print ("FUNCION CUADRATICA RESTA")
def solucionResta ():
    try:
        a = int(input("Ingrese el primer numero:"))
        b = int(input("Ingrese el segundo numero:"))
        c = int(input("Ingrese el tercer numero:"))
    
        resultado =  math.sqrt (b ** b - 4 * a * c)
        resultado1 = -b - resultado
        resultado2 = 2 * a
        resultado3 = resultado1 / resultado2
        print (resultado3)  
    
    except ZeroDivisionError:
        print ("No se puede dividir en cero")
    except ValueError:
        print ("No se puede ingresar una letra ")
      
solucionResta ()

print ("FUNCION CUADRATICA SUMA")
def solucionSuma ():
    a = int(input("Ingrese el primer numero:"))
    b = int(input("Ingrese el segundo numero:"))
    c = int(input("Ingrese el tercer numero:"))
    
    resultado =  math.sqrt (b ** b - 4 * a * c)
    resultado1 = -b + resultado
    resultado2 = 2 * a
    resultado3 = resultado1 / resultado2
    print (resultado3)    
    
solucionSuma ()