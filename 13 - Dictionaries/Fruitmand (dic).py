def fruitmand_maken(lijst):
    mand = {}
    for fruit in lijst:
        mand[len(fruit)] = fruit
    return mand

def fruitmand_inpakken(mand):
    output = []
    for i in range(1, max(mand.keys()) + 1):
        if i in mand:
            output.append(mand[i])
    return output

print(fruitmand_maken(['banaan', 'aardbei', 'kiwi', 'peer', 'appel', 'bes', 'sinaasappel', 'framboos']))
print(fruitmand_inpakken({6: 'banaan', 7: 'aardbei', 4: 'peer', 5: 'appel', 3: 'bes', 11: 'sinaasappel', 8: 'framboos'}))