# input
lengte = float(input('Wat is de lengte van beide personen: '))
naam_1 = input('Wat is de naam van persoon 1: ')
gewicht_1 = float(input('Wat is het gewicht van persoon 1: '))
naam_2 = input('Wat is de naam van persoon 1: ')
gewicht_2 = float(input('Wat is het gewicht van persoon 1: '))

# programma
bmi_1 = gewicht_1 / pow(lengte, 2)
bmi_2 = gewicht_2 / pow(lengte, 2)

if bmi_1 > bmi_2:
    check = bmi_1
    naam = naam_1

else:
    check = bmi_2
    naam = naam_2

if check < 18.5:
    gewicht = 'heeft ondergewicht.'
elif check < 25:
    gewicht = 'heeft een gezond gewicht.'
elif check < 30:
    gewicht = 'heeft overgewicht.'
else:
    gewicht = 'is obees.'

# uitvoer
print(naam, 'heeft het hoogste BMI ({:.2f}) en'.format(check), gewicht)