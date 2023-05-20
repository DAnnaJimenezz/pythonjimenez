diccionario= {"animal": "mono", 
              "clasificacion": "vertebrado",
              "alimentacion": "banano",
              "animal": "mariposa",
              "clasificacion": "invertebrado",
              "alimentacion": "nectar de las flores"}
print (diccionario)

def palabraDiccionario (key, diccionario):
    if key not in diccionario:
        return (f'La palabra clave {key} no esta en este diccionario')
    else:
        a=diccionario [key]
        b= type (a)
        if b is str:
            a="Texto o cadena"
        else:
            b="Numero entero"
        return (f'La palabra clave {key} esta asociada a --> {a} y es tipo {b}')

print (palabraDiccionario(input("Escriba la palbra clave que desea buscar en este diccionario:"), diccionario))
