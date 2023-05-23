d1= {"leon": "lion", 
     "elefante": "elephant", 
     "sapo": "toad",
     "tortuga": "tortoise"}
d2= {"lion": "leon",
     "elephant": "elefante",
     "toad": "sapo",
     "tortoise": "tortuga"}

print (f'Este es el diccionario original de español a ingles:', (d1))
print()
print (f'Este es el diccionario original de ingles a español:', (d2))

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

print()
print("Actualizacion1 del primer dicionario:", agregarEsIn1(d1))
print()
print("Actualizacion2 del primer dicionario:", agregarEsIn2(d1))
print()
print("Actualizacion1 del segundo dicionario:", agregarInEs3(d2))
print()
print("Actualizacion2 del segundo dicionario:", agregarInEs4(d2))