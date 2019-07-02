def geldige_zet(zet):
    output = False
    if len(zet) == 2 and ord('a') <= ord(zet[0]) <= ord('h') and int(zet[1]) <= 8:
        output = True
    elif len(zet) == 3 and ord('a') <= ord(zet[1]) <= ord('h') and int(zet[2]) <= 8 and zet[0] in ('K', 'T', 'D', 'L', 'P'):
        output = True
    return output

def geldige_zetten(zetten):
    output = True
    for zet in zetten:
        if not geldige_zet(zet):
            output = False
    return output


print(geldige_zet('LYKFB'))
print(geldige_zetten(('f8', 'XZJM', 'Pa3', 'Pf3')))