ruilmarkt = {'goud': {'erts', 'wol', 'steen'},
           'wol': {'erts', 'steen', 'hout'},
           'erts': {'hout', 'steen'},
           'steen': {'hout', 'graan'}}

def wisselen_mogelijk(prijzen, aankoop, bezit):
    output = True
    for product in prijzen.get(aankoop):
        if product not in bezit:
            output = False
    return output


def bereken_ruilmiddelen(prijzen, aankopen):
    output = {}
    for aankoop in aankopen:
        for product in prijzen.get(aankoop):
            if product in output:
                output[product] += 1
            else:
                output[product] = 1
    return output


def wisselen(prijzen, aankoop, bezit):
    if wisselen_mogelijk(prijzen, aankoop, bezit):
        for product in prijzen.get(aankoop):
            bezit.remove(product)
        bezit.append(aankoop)
    return bezit

print(wisselen_mogelijk(ruilmarkt, 'steen', ['wol', 'erts']))
print(wisselen_mogelijk(ruilmarkt, 'wol', ['graan', 'erts', 'steen', 'steen', 'erts', 'erts', 'hout', 'goud']))
print(bereken_ruilmiddelen(ruilmarkt, ['wol']))
print(bereken_ruilmiddelen(ruilmarkt, ['goud', 'erts', 'erts']))
print(wisselen(ruilmarkt, 'steen', ['wol', 'erts']))
print(wisselen(ruilmarkt, 'wol', ['graan', 'erts', 'steen', 'steen', 'erts', 'erts', 'hout', 'goud']))
