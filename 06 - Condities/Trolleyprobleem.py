# inputs
hendel = input('Trek je aan de hendel: ')
brug =  input('Duw je de man van de brug: ')

# programma
if hendel == 'ja' and brug == 'ja':
    doden = 2
elif (hendel == 'nee' and brug == 'ja') or (hendel == 'ja' and brug == 'nee'):
    doden = 1
elif hendel == 'nee' and brug == 'nee':
    doden = 5

# uitvoer
print(doden)
