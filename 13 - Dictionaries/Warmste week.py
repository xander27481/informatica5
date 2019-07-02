def gift_inschrijven(gift, giften):
    klas, bedrag = gift
    if klas in giften:
        giften[klas] += bedrag
    else:
        giften[klas] = bedrag
    return giften


print(gift_inschrijven(('5WWI', 78.33),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 82.68}))
print(gift_inschrijven(('5IN', 73.81),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 232.48}))