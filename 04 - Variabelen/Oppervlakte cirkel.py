straal = float(input('straal:'))

pi = 3.14159

oppervlakte_cirkel = pi * (straal ** 2)

uitvoer = "De oppervlakte van een cirkel met straal "
uitvoer += str(straal)
uitvoer += " is "
uitvoer += str(oppervlakte_cirkel)
print(uitvoer)