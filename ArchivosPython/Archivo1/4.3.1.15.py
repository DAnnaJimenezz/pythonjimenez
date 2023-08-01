from os import strerror

counters = {chr(ch): 0 for ch in range(256)}
caracteres_numerico = {chr(ch): 0 for ch in range(ord('0'), ord('9') + 1)} 
caracteres_especiales= {char: 0  for char in "!@#$%^&*()_+-=[]{}|;':,.<>?/`~ "}

file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
            elif char.isdigit(): 
                counters[char] += 1 
            else:
                if char in caracteres_especiales:
                    counters[char] += 1 
    file.close()
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))