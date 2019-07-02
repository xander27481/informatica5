def tel_woorden(zin):
    aantal = 0
    for teken in zin:
        if teken == ' ' or teken == '.':
            aantal += 1
    return aantal

def langste_zin(zin):
    langste = 0
    plaats_punt = zin.find('.')

    while plaats_punt != -1:

        aantal = tel_woorden(zin[:plaats_punt + 1])

        if aantal > langste:
            langste = aantal

        zin = zin[plaats_punt + 2:]
        plaats_punt = zin.find('.')

    return langste



#print(tel_woorden('Ze weet al welke ze wil.'))
#print(tel_woorden('Die.'))
print(langste_zin('hallo. hoe gat het. peeeer er e e re. ik appel.'))