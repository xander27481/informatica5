till  = 20
grootste = 0

def volgende(a):
    if a % 2 == 0:
        return a/2
    else:
        return 3 * a + 1

for getal in range(13, 14):
    aantal = 1
    while getal != 1:
        aantal += 1
        getal = volgende(getal)
    if aantal > grootste:
        grootste = aantal
        start_num = getal

print(start_num)
