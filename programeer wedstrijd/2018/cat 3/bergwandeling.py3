aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    info = input().split()
    breete = int(info[0])
    hoogte = int(info[1])
    kaart, pad = [], {}
    for rij in range(hoogte):
        lijn = []
        lijn += input().split()
        kaart.append(lijn)
# Laagste
    laagste, start_kolom, start_rij = 999, 0, 0
    for rij in range(hoogte):
        for kolom in range(breete):
            if int(kaart[rij][kolom]) < laagste:
                laagste = int(kaart[rij][kolom])
                start_rij = rij
                start_kolom = kolom
# Verplaatsen
    vorige_rij, vorige_kolom, rij, kolom = start_rij, start_kolom, start_rij, start_kolom
    gevonden, letter = True, ord('A')
    pad[(rij, kolom)] = chr(letter)
    while gevonden:
        richtingen, gevonden, letter = {}, False, letter + 1
        if rij != 0 and vorige_rij != rij - 1:
            richtingen['boven'] = [kaart[rij - 1][kolom], rij - 1, kolom]
        if rij != hoogte - 1 and vorige_rij != rij + 1:
            richtingen['onder'] = [kaart[rij + 1][kolom], rij + 1, kolom]
        if kolom != 0 and vorige_kolom != kolom - 1:
            richtingen['links'] = [kaart[rij][kolom - 1], rij, kolom - 1]
        if kolom != breete - 1 and vorige_kolom != kolom + 1:
            richtingen['rechts'] = [kaart[rij][kolom + 1], rij, kolom + 1]

        laagste = min([int(richtingen[x][0]) for x in richtingen if int(richtingen[x][0]) >= int(kaart[rij][kolom])], default='none')

        for value in richtingen.values():
            if int(value[0]) == laagste:
                gevonden = True
                vorige_rij, vorige_kolom, rij, kolom = rij, kolom, value[1], value[2]
                pad[(rij, kolom)] = chr(letter)

# Toon resultaat
    for rij in range(hoogte):
        print(testgeval, end=' ')
        for kolom in range(breete):
            if (rij, kolom) in pad:
                print(pad[(rij, kolom)], end='')
            else:
                print('.', end='')
        print()
