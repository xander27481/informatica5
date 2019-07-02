def hoogtemeters(hoogtes):
    output = []
    for i in range(0, len(hoogtes) - 1):
        output.append(hoogtes[i + 1] - hoogtes[i])
    return output

def dalen_en_stijgen(hoogtes):
    dalen, stijgen = -sum([x for x in hoogtes if x < 0]), sum([x for x in hoogtes if x > 0])
    return dalen, stijgen

'''
def dalen_en_stijgen(hoogtes):
    dalen, stijgen = 0, 0
    for cijfer in hoogtes:
        if cijfer < 0:
            dalen -= cijfer
        else:
            stijgen += cijfer
    return dalen, stijgen
'''
# or



print(hoogtemeters([822, 61, 347, 234, 883, 336]))
print( dalen_en_stijgen([-761, 286, -113, 649, -547]))