# dobbelstenen
aanvaller_1 = int(input('Wat is het nummer van de eerste dobblesteen van de aanvaller: '))
aanvaller_2 = int(input('Wat is het nummer van de tweede dobblesteen van de aanvaller: '))
aanvaller_3 = int(input('Wat is het nummer van de derde dobblesteen van de aanvaller: '))
verdediger_1 = int(input('Wat is het nummer van de eerste dobblesteen van de verdediger: '))
verdediger_2 = int(input('Wat is het nummer van de tweede dobblesteen van de verdediger: '))

# sorteren dobbelstenen van aanvaller
sorteerd_aanvaller_1 = max(aanvaller_1, max(aanvaller_2, aanvaller_3))
sorteerd_aanvaller_3 = min(aanvaller_1, min(aanvaller_2, aanvaller_3))
sorteerd_aanvaller_2 = min(max(aanvaller_1, aanvaller_2), max(aanvaller_2, aanvaller_3), max(aanvaller_1, aanvaller_3))
    #(aanvaller_1 + aanvaller_2 + aanvaller_3) - sorteerd_aanvaller_1 - sorteerd_aanvaller_3


# sorteren dobbelstenen van verdediger
sorteerd_verdideger_1 = max(verdediger_1, verdediger_2)
sorteerd_verdideger_2 = min(verdediger_1, verdediger_2)

# punten
aanvaller_verliest = 0
verdediger_verliest = 0

if sorteerd_aanvaller_1 <= sorteerd_verdideger_1:
    aanvaller_verliest += 1
else:
    verdediger_verliest += 1

if sorteerd_aanvaller_2 <= sorteerd_verdideger_2:
    aanvaller_verliest += 1
else:
    verdediger_verliest += 1

# uitvoer
if aanvaller_verliest == 1:
    print('aanvaller verliest',aanvaller_verliest,'leger, verdediger verliest',verdediger_verliest,'leger')
else:
    print('aanvaller verliest',aanvaller_verliest,'legers, verdediger verliest',verdediger_verliest,'legers')