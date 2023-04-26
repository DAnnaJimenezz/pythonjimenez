n=int(input('ingrese numero'))   #Pide al usuario ingresar un numero 
i=1
while i<n: #Usa while para declarar mientras i sea menor de n haga 
    if i%7==0:   #Usa if y declara numeros multiplos de 7 
        print(f'{i} es multiplo de 7')
    else:
        print(i)
    i+=1