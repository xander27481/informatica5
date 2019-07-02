def woord_frequentie(zin):
    woorden = {}
    zin = zin.lower().split(' ')
    for woord in zin:
        if woord[-1] == '.':
            woord = woord[:-1]
        if woord in woorden:
            woorden[woord] += 1
        else:
            woorden[woord] = 1
    return woorden

def woorden_per_frequentie(zin):
    woorden = {}
    frequentie = woord_frequentie(zin)
    for woord, aantal in frequentie.items():
        if aantal in woorden:
            woorden[aantal] += [woord]
        else:
            woorden[aantal] = [woord]
    return woorden

def meest_gebruikte_woorden(zin):
    frequenties = woorden_per_frequentie(zin)
    return frequenties[max(frequenties.keys())]

print(woord_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))
print(woorden_per_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))
print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))