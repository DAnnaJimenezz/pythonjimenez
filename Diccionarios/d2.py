d1= {"leon": "lion", 
     "elefante": "elephant", 
     "sapo": "toad",
     "tortuga": "tortoise"}
d2= {"lion": "leon",
     "elephant": "elefante",
     "toad": "sapo",
     "tortoise": "tortuga"}

print (f'Este es el diccionario de español a ingles:', (d1))
print()
print (f'Este es el diccionario de ingles a español:', (d2))

def agregarEsIn1 (d1):
    d1 ["cocodrilo"] = "crocodile"
    d1 ["pato"] = "duck"
    return d1 

def agregarEsIn2 (d1):
    d1 ["tucan"] = "toucan"
    d1 ["gallina"] = "hen"
    return d1

def agregarInEs3 (d2):
    d2 ["pig"] = "cerdo"
    d2 ["bear"] = "oso"
    return d2

def agregarInEs4 (d2):
    d2 ["rhinoceros"] = "rinoceronte"
    d2 ["horse"] = "caballo"
    return d2

print (agregarEsIn1 (d1))
print()
print (agregarEsIn2 (d1))
print()
print (agregarInEs3 (d2))
print()
print (agregarInEs4 (d2))

while True:
    print ('1-Actualizacion 1 primer diccionario')
    print ('2-Actualizacion 2 primer diccionario')
    print ('3-Actualizacion 1 segundo diccionario')
    print ('4-Actualizacion 2 segundo diccionario')
    op = int(input("¿Que actualizacion desea realizar?:"))
    if op == "1":
        print ("La actualizacion 1 del primer dicionario es: ", agregarEsIn1 (d1))
    elif op == "2":
        print ("La actualizacion 2 del primer dicionario es: ", agregarEsIn2 (d1))
    elif op == "3":
        print ("La actualizacion 1 del segundo dicionario es: ", agregarEsIn1 (d2))
    elif op == "4":
        print ("La actualizacion 2 del segundo dicionario es: ", agregarEsIn2 (d2))

