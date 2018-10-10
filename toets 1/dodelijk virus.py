from math import pow

# input
minuten = float(input('Hoeveel minuten zijn er al gepaseerd: '))

# programma
toeschouwers = int(50000 * pow(0.5, minuten))

# uitvoer
print(toeschouwers)
