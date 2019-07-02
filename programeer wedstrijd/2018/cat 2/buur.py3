aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    info = input().split(' ')
    breete = int(info[0])
    hoogte = int(info[1])
    kaart, buurlanden = [], {}
# Buurlanden klaar maken
    for rij in range(hoogte):
        lijn = []
        lijn += input()
        for land in lijn:
            if land not in buurlanden:
                buurlanden[land] = []
        kaart.append(lijn)
# Check buurlanden
    for rij in range(hoogte):
        for kolom in range(breete):
            if rij != 0 and kaart[rij - 1][kolom] != kaart[rij][kolom]:
                buurlanden[kaart[rij][kolom]] += kaart[rij - 1][kolom]
            if rij != hoogte - 1 and kaart[rij + 1][kolom] != kaart[rij][kolom]:
                buurlanden[kaart[rij][kolom]] += kaart[rij + 1][kolom]
            if kolom != 0 and kaart[rij][kolom - 1] != kaart[rij][kolom]:
                buurlanden[kaart[rij][kolom]] += kaart[rij][kolom - 1]
            if kolom != breete - 1 and kaart[rij][kolom + 1] != kaart[rij][kolom]:
                buurlanden[kaart[rij][kolom]] += kaart[rij][kolom + 1]
# Verwijder dubbels
    for key in buurlanden.keys():
        buurlanden[key] = list(set(buurlanden[key]))
# Print
    for rij in range(hoogte):
        lijn = ''
        for letter in kaart[rij]:
            lijn += (str(len(buurlanden[letter])) + ' ')
        print(testgeval, lijn.strip())