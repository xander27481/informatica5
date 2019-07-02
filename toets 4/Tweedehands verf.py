def kleur_toevoegen(lijst, kleur):
    if kleur == 'rood':
        lijst[0] += 1
    elif kleur == 'groen':
        lijst[1] += 1
    else:
        lijst[2] += 1
    return lijst

def is_wit(lijst):
    output = False
    if lijst[0] == lijst[1] == lijst[2]:
        output = True
    return output

def verf_verzamelen(kleuren):
    lijst, pot = [0, 0, 0], 0
    while not is_wit(lijst) and pot != len(kleuren) or lijst == [0, 0, 0]:
        lijst = kleur_toevoegen(lijst, kleuren[pot])
        pot += 1
    if is_wit(lijst):
        return pot, lijst


print(kleur_toevoegen([3, 0, 8], 'blauw'))
print(is_wit([2, 3, 2]))
print(verf_verzamelen(['rood', 'rood', 'blauw', 'blauw', 'rood', 'rood', 'rood', 'groen', 'blauw', 'groen', 'groen', 'groen', 'blauw', 'blauw', 'groen', 'blauw']))
print(verf_verzamelen(['groen', 'groen', 'rood', 'groen', 'rood', 'groen', 'groen', 'rood', 'blauw', 'groen', 'groen', 'blauw', 'blauw', 'rood', 'rood', 'rood', 'blauw', 'rood']))