d1 = {"leon": "lion", 
      "elefante": "elephant", 
      "sapo": "toad",
      "tortuga": "tortoise"}

def tuplaAnima1(d1):
    listaEspañol=[]
    listaIngles=[]
    for clave,valor in d1.items():
        listaEspañol.append(clave)
        listaIngles.append(valor)
        tuplaEspañol = tuple(listaEspañol)
        tuplaIngles = tuple(listaIngles)
    return (tuplaEspañol, tuplaIngles)
  
tuplaA, tuplaB= tuplaAnima1 (d1)
print ("La tupla en español son: ", tuplaA)
print ("La tupla en ingles son: ", tuplaB)