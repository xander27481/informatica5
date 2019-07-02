aantal_testgevallen = int(input())

woorden = ('ba', 'di', 'du')

for testgeval in range(1, aantal_testgevallen + 1):
    print(testgeval, end= ' ')
    for aantal in range(5):
        woord = input()
        output = 'naomees'
        if woord[:2] not in woorden or  woord[-2:] not in woorden:
            output = 'onzin'
        for i in range(2, len(woord) - 2, 2):
            check = woord[i:i + 2]
            voor, na = woord[i - 2:i], woord[i + 2:i + 4]
            if voor != check and na != check and voor != na:
                output = 'onzin'
        if not aantal == 4:
            print(output, end=' ')
        else:
            print(output)

# invoer
# 1
# dudubabadudubabadudu
# didudubadududi
# dudubadibadibadu
# ookonzin
# dididudidibadibadididudidi