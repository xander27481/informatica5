# input
getal = int(input('Geef een getal: '))

deler = 1
uitkomst = 0
output = '{} is geen priemgetal'.format(getal)

# programma
while deler < getal and uitkomst != getal // deler:
    deler += 1
    uitkomst = getal / deler
    if uitkomst == 1:
        output = '{} is een priemgetal'.format(getal)

print(output)
