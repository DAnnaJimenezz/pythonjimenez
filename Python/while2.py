x,y= 3,5
while not (x%y==0 or y%x==0):
    x=int (input("Ingrese numero"))
    y=int (input("Ingrese numero"))

print (f'{x} y {y} son factor')
