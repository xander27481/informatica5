import random
random.seed(1)

# start waarden
getal = 22
gok = 0
gok_keer = 0
van = 1
tot = 100

# programma
while gok != getal:
    gok = random.randint(van, tot)
    print('[{},{}] --> computer gokt {}'.format(van, tot, gok))
    if gok < getal:
        van = gok + 1
    else:
        tot = gok - 1
    gok_keer += 1

print('computer had {} pogingen nodig om het getal {} te raden.'.format(gok_keer, getal))
