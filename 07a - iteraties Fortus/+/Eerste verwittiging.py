# input
aantal_gebouwen = int(input('Aantal gebpouwen: '))

gebouw = input('Naam gebouw: ')
hoogte = int(input('Hoogte gebouw: '))
print('{} is zichtbaar van het gelijkvloers tot {} meter.'.format(gebouw, hoogte))

for i in range(aantal_gebouwen - 1):
    gebouw = input('Naam gebouw: ')
    hoogte_2 = int(input('Hoogte gebouw: '))
    if hoogte_2 > hoogte:
        print('{} is zichtbaar van {} meter tot {} meter.'.format(gebouw, hoogte, hoogte_2))
        hoogte = hoogte_2
