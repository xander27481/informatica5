inzet_ = 0

bedrag = int(input('Wat is het start bedrag: '))

inzet = input('Hoeveel zet je in: ')
if inzet == 'stop':
    inzet = 'stop'  # niets moet gebeuren
elif inzet == 'alles':
    inzet = bedrag
else:
    inzet = int(inzet)
keuze = input('Kies zwart of rood: ')
eindigd = input('Op welk kleur land de bal: ')

while inzet_ != 'stop' and inzet <= bedrag:
    if keuze == eindigd and inzet <= bedrag:
        bedrag = bedrag + inzet
    elif inzet <= bedrag:
        bedrag = bedrag - inzet
    print(inzet)
    print(bedrag)
    inzet_ = input('Hoeveel zet je in: ')
    if inzet_ == 'stop':
        inzet_ = 'stop'  # niets moet gebeuren
    elif inzet_ == 'alles':
        inzet = bedrag
    else:
        inzet = int(inzet)
    keuze = input('Kies zwart of rood: ')
    eindigd = input('Op welk kleur land de bal: ')

if inzet > bedrag:
    print('Je kunt geen {} dollar inzetten als je maar {} dollar hebt.'.format(inzet, bedrag))
