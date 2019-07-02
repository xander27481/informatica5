def dronken_voeren(woord):
    nieuw = ''
    # Je hebt een BOB: de eerste letter van het woord drinkt niet en neem je gewoon over.
    nieuw += woord[0]
    for i in range(1, len(woord)):
        if i % 2 == 0:
            nieuw += woord[i].upper()
        elif nieuw[-1] in 'AEIOU':
            nieuw += woord[i].upper()
        else:
            nieuw += woord[i].lower()
    return nieuw

dronken_voeren('kannenKIJKER')