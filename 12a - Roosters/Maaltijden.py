def dagprijs(lijst):
    prijs = 0
    for maaltijd in range(0, len(lijst), 2):
        if lijst[maaltijd] == 'middagmaal':
            prijs += (5.3 * lijst[maaltijd + 1])
        elif lijst[maaltijd] == 'soep':
            prijs += (1.7 * lijst[maaltijd + 1])
        else:
            prijs += (2.3 * lijst[maaltijd + 1])
    return prijs

def weekprijs(weeklijst):
    prijs = 0
    for lijst in weeklijst:
        prijs += dagprijs(lijst)
    return prijs

print(dagprijs(('middagmaal', 2, 'soep', 2, 'vieruurtje', 2)))
print(weekprijs((('middagmaal', 2, 'soep', 2, 'vieruurtje', 2), ('middagmaal', 1, 'soep', 1), ('soep', 3, 'vieruurtje', 3), ('middagmaal', 3, 'soep', 1), ('middagmaal', 3, 'soep', 3, 'vieruurtje', 1))))