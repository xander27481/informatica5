# input
keer = int(input('aantal getallen: '))
som = 0
max_ = 0

getal = int(input('getal: '))
som = getal
maximun = getal

for i in range(keer - 1):
    getal = int(input('getal: '))
    # kan ook
    # maximun = max(maximun, getal)
    if getal > maximun:
        maximun = getal
    som += getal

gem = round((som/keer), 2)
# rond oaf to op 2 maar als het nul is laat het het vallen
print('Het grootste getal is {:d} en het gemiddelde is {}'.format(maximun, gem))
