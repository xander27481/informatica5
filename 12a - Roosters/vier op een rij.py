def printbaar_rek(bord):
    geprint_bord = ''
    for rij in range(-1, -len(bord) - 1, -1):
        geprint_rij = ''
        for kolom in range(len(bord[rij])):
            geprint_rij += bord[rij][kolom]
        geprint_bord += (geprint_rij + '\n')

    return geprint_bord.strip()

def speel(kleur, speel_kolom, bord):
    speel_rij = 0
    for rij in range(-1, -len(bord) - 1, -1):
        if bord[rij][speel_kolom] == 'O':
            speel_rij -= 1
    bord[speel_rij][speel_kolom] = kleur
    return bord


print(printbaar_rek([['R', 'R', 'R', 'R', 'G'], ['G', 'G', 'R', 'G', 'R'], ['O', 'G', 'O', 'O', 'O'], ['O', 'R', 'O', 'O', 'O']]))
print(speel('R',0,[['R', 'R', 'R', 'G', 'R'], ['G', 'O', 'G', 'R', 'G'], ['G', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))