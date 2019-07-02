def ik_heb_gemoord(taak, moordenaar):
    if len(taak) != 1:
        vermoord = taak.index(moordenaar) + 1
        vermoord %= len(taak)

        taak[vermoord:vermoord + 1] = []

        nieuwe = taak.index(moordenaar) + 1
        nieuwe %= len(taak)

        return taak[nieuwe], taak
    else:
        return moordenaar, taak


def ik_ben_vermoord(taak, vermoord):
    if len(taak) != 1:
        nieuwe = taak.index(vermoord)

        taak[taak.index(vermoord):taak.index(vermoord) + 1] = []

        nieuwe %= len(taak)

        return taak[nieuwe], taak
    else:
        return vermoord, taak

print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'korneel'))
print(jij_bent_vermoord(['jan', 'piet', 'joris'],'joris'))