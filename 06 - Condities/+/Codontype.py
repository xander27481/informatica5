# input
codon = input('Geef de codon in: ')

# programma
if codon == 'AUG':
    omschrijving_codon = 'start'
elif codon == 'UAG' or codon == 'UGA' or codon == 'UAA':
    omschrijving_codon = 'stop'
elif len(codon) == 3:
    omschrijving_codon = 'gewoon'
else:
    omschrijving_codon = 'ongeldig'

# uitvoer
print('Het codon', codon, 'is een', omschrijving_codon, 'codon.')
