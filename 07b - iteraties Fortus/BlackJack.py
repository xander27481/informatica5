kaart = int(input('Welke kaart trok je: '))
som = kaart

while kaart != 0 and som < 21:
    kaart = int(input('Welke kaart trok je: '))
    som += kaart

if som == 21:
    print('Gewonnen!')
elif som > 21:
    print('Verbrand ({})'.format(som))
else:
    print('Voorzichtig gespeeld ({})'.format(som))