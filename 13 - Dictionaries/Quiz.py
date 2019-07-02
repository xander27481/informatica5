def verlaat_ploeg(persoon, team, ploegen):
    ploegen[team].remove(persoon)
    if len(ploegen[team]) == 0:
        ploegen.pop(team)
    return ploegen

def vervoegt_ploeg(persoon, team, ploegen):
    if team in ploegen:
        ploegen[team].append(persoon)
    else:
        ploegen[team] = [persoon]
    return ploegen

print(verlaat_ploeg('Tom','Sinbox',{'Sinbox': ['An', 'Tom', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
print(vervoegt_ploeg('Els','Sinbox',{'Sinbox': ['An', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
print(vervoegt_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
print(verlaat_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))