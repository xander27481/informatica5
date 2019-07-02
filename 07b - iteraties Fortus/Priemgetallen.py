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


# is modulo 0 bij het delen van n door alle getallen van 2 tot het getal zelf.
# n = int(input('priemgetal: '))
#
# #is modulo 0 bij het delen van n door alle getallen van 2 tot getal zelf
# #zolang de modulo verschillend van 0 is zijn we goed bezig
#
# i = 2
# while n // i != n/i and i <= (n // 2) + 1:
#     i += 1
#
# if i == n // 2 + 1:
#     print(str(n) + ' is een priemgetal')
# else:
#     print(str(n) + ' is geen priemgetal')