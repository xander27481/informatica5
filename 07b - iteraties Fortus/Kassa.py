kost = 0
prijs = float(input('Geef de prijs in: '))
while prijs != 0:
    kost += prijs
    prijs = float(input('Geef de prijs in: '))

print('De totale prijs is € {:.2f}'.format(kost))