#[], {}, (), {()}      #Las llaves representan las listas, las corcheas para conjuntos de elementos unicos, el parantesis para llamar una funcion, y las ultimas para las tuplas
x=100
print(type(x)) #Type nos dice que tipo de dato se esta manejando
x='Soacha'
print(type(x))
lista=['python',100,[1,2,3,[]],'a'] #Declara la lista con diferentes elementos 
print(type(lista))
print(len(lista)) #Funcion len para la longitud o tamaño de la lista 
print(lista[0]) #Se utiliza para imprimir un elemento en especifico 
print(lista[1])
print(lista[3])
print(lista[-4])

del lista[-2] #La funcion del se utiliza para eliminar un elemento de la lista 
print(lista)

"""
cuenta1=cuenta()   
cuenta2=cuenta()      
cuenta3=cuenta()     # Esto es una funcion ya que no esta enlazado ni tiene un punto y realiza algo en especifico
cuenta1.deposit()
print(type(cuenta1))
cuenta2.deposit()    #Esto es un metodo ya que tiene un punto y esta enlazado directamente con un objeto de una clase
cuenta3.deposit()
"""