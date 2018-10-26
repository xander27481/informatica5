# input
aantal_getal = int(input('Het hoeveelste getal wil je? '))

getal_1 = 0
getal_2 = 1

for i in range(2, aantal_getal):
    getal_1, getal_2 = getal_2, getal_1 + getal_2

print(getal_2)