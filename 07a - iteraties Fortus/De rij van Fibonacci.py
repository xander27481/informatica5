# input
aantal_getal = int(input('Het hoeveelste getal wil je? '))

getal_1 = 0
getal_2 = 1
# programma
if aantal_getal == 1:
    getal = 1

for i in range(1, aantal_getal):
    getal = getal_1 + getal_2
    getal_1 = getal_2
    getal_2 = getal

print(getal)