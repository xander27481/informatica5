def volgende_rij(vorige_rij):
    nieuwe_rij = []
    print('------------------')
    for i in range(len(vorige_rij) - 1):
        print(vorige_rij[i], vorige_rij[i + 1])
        if vorige_rij[i] == vorige_rij[i + 1]:
            nieuwe_rij.append(vorige_rij[i])
        elif (vorige_rij[i] == 'G' and vorige_rij[i + 1]) == 'Y' or (vorige_rij[i] == 'Y' and vorige_rij[i + 1] == 'G'):
            nieuwe_rij.append('R')
        elif (vorige_rij[i] == 'Y' and vorige_rij[i + 1] == 'R') or (vorige_rij[i] == 'R' and vorige_rij[i + 1] == 'Y'):
            nieuwe_rij.append('G')
        else:
            nieuwe_rij.append('Y')
    return nieuwe_rij

def driehoek(rij):
    lijst = [rij]
    while len(lijst[-1]) != 1:
        lijst.append(volgende_rij(lijst[-1]))
    return lijst

def kleuren(lijst):
    aantal_G, aantal_Y, aantal_R = 0, 0, 0
    for rij in range(len(lijst)):
        for kolom in range(len(lijst[rij])):
            if lijst[rij][kolom] == 'G':
                aantal_G += 1
            elif lijst[rij][kolom] == 'Y':
                aantal_Y += 1
            else:
                aantal_R += 1
    return aantal_G, aantal_R, aantal_Y

print(volgende_rij(['Y', 'R', 'R', 'Y', 'Y', 'G', 'Y', 'R', 'R']))
print(driehoek(['G', 'G', 'G', 'G', 'G']))
print(kleuren([['G', 'G', 'G', 'G', 'G'], ['G', 'G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G'], ['G']]))