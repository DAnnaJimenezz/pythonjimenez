num1,num2=100,50  #Se asignan los valores para realizar las distintas operaciones 
print('1-sumar')  #Operacion aritmetica basica 
print('2-restar')  #Operacion aritmetica basica 
print('3-multiplicar') #Operacion aritmetica basica 
print('4-dividir') #Operacion aritmetica basica 
print('5-residuo') #Operacion aritmetica basica 
op=int(input('que operacion?'))  #El usuario puede elegir que operacion hacer, mediante la variable (op)
match op:     #Las siguientes lineas se utiliza el (match) y (case) las cuales ayudan a realizar multiples comparaciones de igualdad, el case se compara con (op) la cual es el numero de la operacion deseada por el usuario
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)# //  /
    case 5:    
        print(num1%num2)