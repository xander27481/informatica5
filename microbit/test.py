pos = [1, 1]
soorten = {'blok_s': [[1]], 'blok_m': [[1,1], [1,1]]}
bord = [[0 for rij in range(5)] for kolom in range(5)]

while True:
    input()
    toevoegen = soorten.get('blok_m')
    for rij in range(len(toevoegen)):
        for kolom in range(len(toevoegen[0])):
            print(rij, kolom)
            print(pos[0], pos[1])
            print()
            bord[pos[0] + rij][pos[1] + kolom] = toevoegen[rij][kolom]
    print(bord)