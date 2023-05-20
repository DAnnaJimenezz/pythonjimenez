d1 = {"leon": "lion", "elefante": "elephant", "sapo": "toad","tortuga": "tortoise"}

def tuplaAnimal1 (d1):
  listaEspañol= []
  listaIngles= []
  for clave, valor in d1.items():
    listaEspañol.append (clave)
    listaIngles.append (valor)
    tuplaEspañol = tuple(listaEspañol)
    tuplaIngles = tuple(listaIngles)
    return (tuplaEspañol, tuplaIngles)
  
tuplaA, tuplaB = tuplaAnimal1 (d1)
print ("La tupla de animales en español son:", tuplaA)
print ("La tupla de animales en ingles son:", tuplaB)