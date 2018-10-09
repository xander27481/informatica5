# input
temperatuur = float(input('De temperatuur van de ster: '))
lichtkracht = float(input('De lichtkracht van de ster: '))

# programma
if (temperatuur > 3000 and lichtkracht < 0.0001) or (temperatuur > 5000 and lichtkracht < 0.01):
    type_ster = 'witte dwergen'
elif temperatuur < 6000 and 10 < lichtkracht < 100:
    type_ster = 'reuzen'
elif temperatuur < 7500 and 100 < lichtkracht < 1000:
    type_ster = 'heldere reuzen'
elif 10000 > lichtkracht > 1000:
    type_ster = 'superreuzen (b)'
elif lichtkracht > 10000:
    type_ster = 'superreuzen (a)'
else:
    type_ster = 'hoofdreeks'

# uitvoer
print(type_ster)
