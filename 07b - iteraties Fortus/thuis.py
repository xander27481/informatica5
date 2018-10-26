bod = float(input('startprijs: '))
doorgedraaid = float(input('doorgedraaid onder: '))

akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

# zolang (niemand akkord is) EN (er kan noch iets van de prijs worden gedaan
while (not akkoord) and (bod >= doorgedraaid + 0.01):
    # doe van prijs
    bod -= 0.01
    # nu iemand akkoord
    akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

if akkoord:
    print('verkocht aan {:.2f}'.format(bod))
else:
    print('doorgedraaid')