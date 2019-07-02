#kennissen = {'Eva': {'Margaux', 'Arno'}, 'Arno': {'Eva', 'Jens'}, 'Jens': {'Margaux', 'Eva'}, 'Margaux': set()}

def vriend_of_kennis(relaties, a, b):
    output = '{} en {} kennen elkaar niet'.format(a, b)
    if b in relaties.get(a):
        output = '{} kent {}'.format(a, b)
    if a in relaties.get(b) and output == '{} en {} kennen elkaar niet'.format(a, b):
        output = '{} kent {}'.format(b, a)
    elif a in relaties.get(b):
        output = '{} en {} zijn vrienden'.format(a, b)
    return output

def unieke_kennissen(relaties, a, b):
    output = relaties.get(a).union(relaties.get(b)).difference(relaties.get(a).intersection(relaties.get(b)))
    output = output.difference({a, b})
    return output

def bekendheid(relaties):
    personen = {}
    for value in relaties.values():
        for persoon in value:
            if persoon in personen:
                personen[persoon] += 1
            else:
                personen[persoon] = 1
    return personen

def meest_gekende(lijst):
    hoogste = max(lijst.values())
    bekenste = [y for y, x in lijst.items() if x == hoogste]
    return bekenste

kennissen = {'Eva': {'Margaux', 'Arno'}, 'Arno': {'Eva', 'Jens'}, 'Jens': {'Margaux', 'Eva'}, 'Margaux': set()}
'''
print(vriend_of_kennis(kennissen, 'Arno', 'Eva'))
print(vriend_of_kennis(kennissen, 'Margaux', 'Eva'))
print(unieke_kennissen(kennissen, 'Arno', 'Eva'))
#print(kennissen)
print(unieke_kennissen(kennissen, 'Eva', 'Margaux'))
#kennissen = {'Eva': {'Margaux', 'Arno'}, 'Arno': {'Eva', 'Jens'}, 'Jens': {'Margaux', 'Eva'}, 'Margaux': set()}
'''
print('------------')
print(unieke_kennissen(kennissen, 'Eva', 'Jens'))
print(unieke_kennissen(kennissen, 'Arno', 'Margaux'))
print(unieke_kennissen(kennissen, 'Arno', 'Jens'))
print('------------')
'''
#kennissen = {'Eva': {'Margaux', 'Arno'}, 'Arno': {'Eva', 'Jens'}, 'Jens': {'Margaux', 'Eva'}, 'Margaux': set()}
print(bekendheid(kennissen))
print(meest_gekende({'Margaux': 2, 'Arno': 1, 'Eva': 2, 'Jens': 1}))
print(kennissen)
'''