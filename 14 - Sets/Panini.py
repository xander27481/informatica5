def verzamel(nieuw, boek, dubbels):
    if nieuw not in boek:
        boek.add(nieuw)
    else:
        if nieuw in dubbels.values():
            plaats = 0
            for key, value in dubbels.items():
                if value == nieuw and len(dubbels[plaats]) == 0:
                    dubbels.pop(value)
                elif value == nieuw:
                    dubbels[key].remove(nieuw)
            if plaats + 1 in dubbels:
                dubbels[plaats + 1] += nieuw
            else:
                dubbels[plaats + 1] = nieuw
        elif 1 in dubbels:
            dubbels[1] += nieuw
        else:
            dubbels[1] = nieuw
    return boek, dubbels


'''
def verzamel(naam, boek, dubbels):
    if naam not in boek:
        boek.add(naam)
    else:
        for key, item in dubbels.items():
            if naam == item:
                print('dd')
                dubbels[key + 1] = naam
    return boek, dubbels
'''

print(verzamel('Bosmans',set(),{}))
print(verzamel('Weber',{'Bosmans'},{}))
print(verzamel('Bosmans',{'Weber', 'Bosmans'},{1: 'Bosmans'}))