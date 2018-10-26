############################### SEED WAS ANDERS ###########################


import random
random.seed(1)

# start waarden
getal = 18
gok = 0
gok_keer = 0
van = 1
tot = 100
gokken = [73, 9, 26, 13, 21, 20, 17, 19, 18]

# programma
while gok != getal:
    gok = gokken[gok_keer]
    print('[{},{}] --> computer gokt {}'.format(van, tot, gok))
    if gok < getal:
        van = gok + 1
    else:
        tot = gok - 1
    gok_keer += 1

print('computer had {} pogingen nodig om het getal {} te raden.'.format(gok_keer, getal))
