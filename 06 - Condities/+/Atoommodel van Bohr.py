# input
elektronen = int(input('Hoeveel elektronen zijn er: '))

# program
if elektronen <= 2:
    schil = 'K'
elif elektronen <= 10:
    schil = 'L'
elif elektronen <= 28:
    schil = 'M'
elif elektronen <= 60:
    schil = 'N'
elif elektronen <= 92:
    schil = 'O'
elif elektronen <= 124:
    schil = 'P'
elif elektronen <= 156:
    schil = 'Q'


# uitvoer
print('De ' + str(schil) + '-schil is de buitenste schil van een stabiel atoom met ' + str(elektronen) + ' elektronen.')