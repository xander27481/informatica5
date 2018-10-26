# input
getal = input('Wat is het getal: ')

som = 0
# programma
for i in getal:
    som += int(i)

if int(getal) / som == int(getal) // som:
    print(getal + ' is een Harshadgetal')
else:
    print(getal + ' is geen Harshadgetal')