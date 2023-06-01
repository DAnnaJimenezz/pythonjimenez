def FunB():
    diccionario = {}  # Crear un diccionario vacío
    
    while True:
        clave = input("Ingresa una clave (o 'salir' para terminar): ")
        if clave == "salir":
            break
        
        valor = input("Ingresa un valor: ")
        diccionario[clave] = valor
    
    return diccionario

# Ejemplo de uso:
diccionario_usuario = FunB()
print("Diccionario resultante:", diccionario_usuario)