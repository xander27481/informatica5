# input
kleur_a = input('welke kleur heeft de hoed van persoon 1: ')
kleur_b = input('welke kleur heeft de hoed van persoon 2: ')
omgekeerde = int(input('wie zegt het omgekeerde: '))

# programma
if omgekeerde == 1 and kleur_b == 'zwart':
    antwoord_a = 'wit'
    antwoord_b = kleur_a
elif omgekeerde == 1 and kleur_b == 'wit':
    antwoord_a = 'zwart'
    antwoord_b = kleur_a
elif omgekeerde == 2 and kleur_a == 'zwart':
    antwoord_a = kleur_b
    antwoord_b = 'wit'
elif omgekeerde == 2 and kleur_a == 'wit':
    antwoord_a = kleur_b
    antwoord_b = 'zwart'

# uitvoer
print(antwoord_a)
print(antwoord_b)
