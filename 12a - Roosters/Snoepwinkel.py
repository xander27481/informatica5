from operator import itemgetter

def bereken_prijs(lijst):
    prijs = 0
    for i in range(len(lijst)):
        prijs += lijst[i][1]
    return prijs

def winkelbriefje(lijst):
    briefje = []
    for i in range(len(lijst)):
        briefje.append(lijst[i][0])
    return briefje

def sorteer(lijst):
    lijst.sort(key=itemgetter(1))
    return lijst


print(bereken_prijs([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))
print(winkelbriefje([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))
print(sorteer([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))