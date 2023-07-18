dict = {'perro':'dog', 'gato':'cat', 'sapo': 'toad'}
try:
    clave = input("Ingrese la clave del diccionario que desea buscar en el diccionario:")
    valor = dict [clave]
    print (f'El valor de {clave} es {valor}')

except KeyError:
    print ("No se puede enocontrar el elemento")