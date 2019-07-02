aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    info = input().split()
    aantal_boekenkasten = int(info[0])
    kasten = [int(x) for x in info[1:]]
    kasten.sort(reverse=True)
    aantal_boeken = int(input())
    boeken = []
    for i in range(aantal_boeken):
        info = input().split(' ')
        dikte, boek = int(info[0]) , ' '.join(info[1:])
        boeken.append([boek, dikte])
        boeken.sort()
    plank = 0
    while plank < aantal_boekenkasten and len(boeken) != 0:
        if kasten[plank] >= boeken[0][1]:
            kasten[plank] -= boeken[0][1]
            boeken.pop(0)
        else:
            plank += 1
    if aantal_boeken == 0:
        output = 0
    elif len(boeken) == 0:
        output = plank + 1
    else:
        output = 'ONMOGELIJK'

    print(testgeval, output)