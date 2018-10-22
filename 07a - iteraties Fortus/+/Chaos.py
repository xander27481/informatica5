# input
d = float(input('Wat was de initiële populatiedichtheid: '))
r = float(input('Wat is de vruchtbaarheids parameter: '))
s = int(input('Over hoeveel tijdstappen wil de populatie dichtheid simuleren: '))

# programma
print(d)
for i in range(s - 1):
    d = t = r * d * (1 - d)
    print(d)
