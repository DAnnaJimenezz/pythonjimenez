import random
tam = random.randint (5,15)
l1 = ()
l2 = ()
l3 = ()

for i in range (tam):
    num=random.randrange (100)
    l1 += (num,)

print (l1)

l2 = l1 [:5]

print (l2)

l3 = l1 [5:]

print (l3)

