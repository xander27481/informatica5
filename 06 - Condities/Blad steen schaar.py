# invoer
persoon_1 = input('persoon 1: ')
persoon_2 = input('persoon 2: ')

# programma
if persoon_1 == persoon_2:
    uitvoer = 'onbeslist'
elif (persoon_1 == 'blad' and persoon_2 == 'steen') or (persoon_1 == 'steen' and persoon_2 == 'schaar'):
    uitvoer = 'speler 1 wint'
elif persoon_1 == 'schaar' and persoon_2 == 'blad':
    uitvoer = 'speler 1 wint'
elif (persoon_2 == 'blad' and persoon_1 == 'steen') or (persoon_2 == 'steen' and persoon_1 == 'schaar'):
    uitvoer = 'speler 2 wint'
elif persoon_2 == 'schaar' and persoon_1 == 'blad':
    uitvoer = 'speler 2 wint'

# uitvoer
print(uitvoer)