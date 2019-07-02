gewonnen = 0
woord_2 = ''

woord = input('Wat is het woord: ')
inzet= int(input('Wat is de inzet: '))

letter = input('Gok een letter: ')
while letter in woord and letter not in woord_2:
    woord_2 += letter
    gewonnen += inzet
    letter = input('Gok een letter: ')

print(gewonnen)
