def dubbels(lijst):
    dubbel = []
    for i in range(len(lijst)):
        if lijst[i] in lijst[i + 1::] and lijst[i] not in dubbel:
    return dubbel

''' # enkel in deen allemaal cijfers/woorden
def dubbels(lijst):
    lijst.sort()
    dubbel = []
    for i in range(len(lijst)):
        if lijst[i] == lijst[i + 1] and lijst[i] not in dubbel:
    return dubbel
'''

dubbels([2, 'joris'])
dubbels(['joris', 'jan', (0, 1), 2, 1, 1, 1])
dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris'])