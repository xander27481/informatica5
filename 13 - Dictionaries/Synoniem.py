def synoniemen(zin, dictionary):
    zin = zin.split(' ')
    for i in range(len(zin)):
        if zin[i] in dictionary:
            zin[i] = dictionary[zin[i]]
    return ' '.join(zin)

print(synoniemen('op school heb je best geen slechte manieren',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))