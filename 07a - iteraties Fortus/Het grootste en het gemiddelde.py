# input
keer = int(input('aantal getallen: '))
som = 0
max_ = 0


for i in range(keer):
    getal = int(input('getal: '))
    if i == 0:
        max_ = getal
    if getal > max_:
        max_ = getal
    som += getal

gem = round((som/keer), 2)
print('Het grootste getal is {:d} en het gemiddelde is {}'.format(max_, gem))
