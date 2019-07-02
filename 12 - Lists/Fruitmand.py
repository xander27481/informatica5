def fruitstuk_toevoegen(mand, fruit):
    for i in range(len(mand)):
        if len(mand[i]) == len(fruit):
            mand[i] = fruit
        elif len(mand[i]) > len(fruit) and fruit not in mand:
            mand.insert(i, fruit)
        elif i == len(mand) - 1 and fruit not in mand:
            mand.append(fruit)
    return mand

def maak_fruitmand(lijst):
    mand = [lijst[0]]
    for i in range(1, len(lijst)):
        mand = fruitstuk_toevoegen(mand, lijst[i])
    return mand

print(fruitstuk_toevoegen(['kiwi'],'peer'))
print(fruitstuk_toevoegen(['bes', 'peer', 'framboos', 'sinaasappel'],'appel'))
print(maak_fruitmand(['kiwi', 'peer', 'kiwi', 'peer', 'kiwi']))
print(maak_fruitmand(['bes', 'appel', 'framboos']))