def binnen_of_buiten(midden, cirkel, punt):
    straal = pow(pow(midden[0] - cirkel[0], 2) + pow(midden[1] - cirkel[1], 2), 1/2)
    afstand = pow(pow(midden[0] - punt[0], 2) + pow(midden[1] - punt[1], 2), 1/2)
    if afstand > straal:
        plaats = 'buiten'
    elif afstand == straal:
        plaats = 'op'
    else:
        plaats = 'binnen'
    return plaats, round(afstand, 4)

print(binnen_of_buiten((7, -1),(-9, -32),(12, -48)))