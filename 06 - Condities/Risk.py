# dobbelstenen
aanvaller_1 = input('Wat is het nummer van de eerste dobblesteen van de aanvaller: ')
aanvaller_2 = input('Wat is het nummer van de tweede dobblesteen van de aanvaller: ')
aanvaller_3 = input('Wat is het nummer van de derde dobblesteen van de aanvaller: ')
verdediger_1 = input('Wat is het nummer van de eerste dobblesteen van de verdediger: ')
verdediger_2 = input('Wat is het nummer van de tweede dobblesteen van de verdediger: ')

# sorteren dobbelstenen van aanvaller
if aanvaller_1 >= aanvaller_2 and aanvaller_1 >= aanvaller_3:
    if aanvaller_3 > aanvaller_2:
        hulp = aanvaller_2
        aanvaller_2 = aanvaller_3
        aanvaller_3 = hulp

elif aanvaller_2 >= aanvaller_1 and aanvaller_2 >= aanvaller_3:
    hulp = aanvaller_1
    aanvaller_1 = aanvaller_2
    aanvaller_2 = hulp
    if aanvaller_3 > aanvaller_2:
        hulp = aanvaller_2
        aanvaller_2 = aanvaller_3
        aanvaller_3 = hulp

elif aanvaller_3 >= aanvaller_1 and aanvaller_3 >= aanvaller_2:
    hulp = aanvaller_1
    aanvaller_1 = aanvaller_3
    aanvaller_3 = hulp
    if aanvaller_3 > aanvaller_2:
        hulp = aanvaller_2
        aanvaller_2 = aanvaller_3
        aanvaller_3 = hulp


# sorteren dobbelstenen van verdediger
if verdediger_2 >= verdediger_1:
    hulp = verdediger_1
    verdediger_1 = verdediger_2
    verdediger_2 = hulp

# punten
aanvaller_verliest = 0
verdediger_verliest = 0

if aanvaller_1 <= verdediger_1:
    aanvaller_verliest += 1
else:
    verdediger_verliest += 1

if aanvaller_2 <= verdediger_2:
    aanvaller_verliest += 1
else:
    verdediger_verliest += 1

# uitvoer
if aanvaller_verliest == 1:
    print('aanvaller verliest',aanvaller_verliest,'leger, verdediger verliest',verdediger_verliest,'leger')
else:
    print('aanvaller verliest',aanvaller_verliest,'legers, verdediger verliest',verdediger_verliest,'legers')