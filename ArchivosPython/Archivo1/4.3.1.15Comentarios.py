from os import strerror #Importa la funcion strerror del modulo os la cual se utiliza para obtener y describir el error 

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)} #Crea un diccionario llamado counters con clave y valor con letras del abecedario como clave y el valor incializado en 0, en el for itera desde el valor de la letra a, hasta el valor de la letra z
file_name = input("Ingresa el nombre del archivo a analizar: ") #Crea una variable file_name y le pide al usuario que ingrese por teclado

try: #Abre el bloque de codigo try

    file = open(file_name, "rt") #Abre el archivo llamado file_name y con el comando rt no da a entender que esta en modo texto
    for line in file: #Se recorre con un for para que lea linea a linea el archivo
        for char in line: #Recorre cada linea caracter por caracter
            if char.isalpha(): #Verifica si el caracter es una letra con el metodo isalpha () 
                counters[char.lower()] += 1 #Actualiza el contador del diccionario y utiliza el metodo lower () para convertirlas en minusculas 
    file.close() #Cierra el archivo utilizando close 
    for char in counters.keys(): #Con el metodo keys () recorre el diccionario counters por clave y valor
        c = counters[char] #Se crea una variable llamada c a la cual se asinga counters[char] donde char sera una letra del abecedario y una clave del diccionario counters
        if c > 0: #Verifica  si la char esta una vez en el texto si esto es verdadero el bloque seguira ejecutandose, de lo contrario no
            print(char, '->', c) # Si la condicion se cumple se imprimira el mensaje de la letra (char) seguido de la flecha, seguido de la frecuencia 
    
except IOError as e: #Ciera con el exept donde nos indica el error IOError 
    print("Se produjo un error de E/S: ", strerror(e.errno)) #Imprime en pantalla el mensaje dado si se da el error, y strerror(e.errno) es utilizado para dar una descripccion de problema 