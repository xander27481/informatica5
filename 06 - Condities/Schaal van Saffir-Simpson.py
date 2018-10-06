# input
windsnelheid = int(input('Windselheid: '))

# programma
if windsnelheid >= 119 and windsnelheid <= 153:
    categorie = 1
elif windsnelheid >= 154 and windsnelheid <= 177:
    categorie = 2
elif windsnelheid >= 178 and windsnelheid <= 209:
    categorie = 3
elif windsnelheid >= 210 and windsnelheid <= 249:
    categorie = 4
else:
    categorie = 5

# uitvoer
if windsnelheid < 119:
    print('geen orkaan')
else:
    print('categorie',categorie)