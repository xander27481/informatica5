lijst = []

kleur = input()

while kleur != 'STOP':
    if kleur == '?':
        if len(lijst) != 0:
            print(lijst.pop(0))
    else:
        lijst. append(kleur)

    kleur = input()