woord_1 = input()
woord_2 = input()

prefix = sufix = ''

for i in range(len(woord_1)):
    if woord_1[i] == woord_2[i]:
        prefix += woord_1[i]
    else:
        break

for i in range(-1, -len(woord_1) - 1, -1):
    if woord_1[i] == woord_2[i]:
        sufix = woord_1[i] + sufix
    else:
        break

if len(woord_1) > len(woord_2):
    midden_1 = woord_1[len(prefix):-len(sufix)]
    midden_2 = center(woord_2[len(prefix):-len(sufix)], len(woord_1))
else:
    midden_1 = center(woord_1[len(prefix):-len(sufix)], len(woord_2))
    midden_2 = woord_2[len(prefix):-len(sufix)]

    print('{}┏{}┓'.format(len(prefix) * ' ', midden_1,))
    print('{}┫{}┣{}'.format(prefix, (len(langst) - len(sufix) - len(prefix)) * ' ', sufix))
    print('{}┗{}┛'.format(len(prefix) * ' ', midden_2))