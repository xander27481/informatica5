'''
def nieuw_kaartspel(kleuren, cijfers):
    output = []
    for kleur in kleuren:
        for cijfer in cijfers:
            output.append(kleur + cijfer)
    return output
'''

def nieuw_kaartspel(kleuren, cijfers):
    output = [x + y for x in kleuren for y in cijfers]
    return output


def splits_kaartspel(lijst):
    helft1, helft2 = [lijst[i] for i in range(len(lijst) - 1) if i < len(lijst) // 2], [lijst[i] for i in range(len(lijst)) if i >= len(lijst) // 2]
    return helft1, helft2

def faro_shuffle(lijst1, lijst2):
    output = []
    for i in range(len(lijst1)):
        output.append(lijst1[i])
        output.append(lijst2[i])
    if len(lijst2) > len(lijst1):
        output.append(lijst2[-1])
    return output

print(nieuw_kaartspel(['dood ', 'liefde ', 'tijd '],['0', '1']))
print(splits_kaartspel(['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1']))
print(splits_kaartspel(['blad 1', 'blad 2', 'blad 3', 'steen 1', 'steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']))
print(faro_shuffle(['dood 0', 'dood 1', 'liefde 0'],['liefde 1', 'tijd 0', 'tijd 1']))
print(faro_shuffle(['blad 1', 'blad 2', 'blad 3', 'steen 1'],['steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']))