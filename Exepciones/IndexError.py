try:
    l1 = [3,8,10,6,2]
    x = l1 [int(input("Ingrese el indice que desea buscar de la lista:"))]
    print (f'El indice ingresado si se encuentra en la lista, {l1}')
    
except IndexError:
    print ("No se puede econtrar el indice, por que no ahi nada en la lista")      