#¿Cuáles y cuántos son los números primos comprendidosentre 1 y 1000?

for num in range (1,1000 ):
    if num >1:
        for i in range (2, num):
            if (num%i)==0:
                break
        else:
            print (num)
