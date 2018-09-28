t = float(input('luchttemperatuur: '))
w = (float(input('windsnelheid: '))) / 3.6

gevoels_temperatuur = 13.12 + (0.6215 * t) + ((0.3965 * t - 11.37)* pow(3.6 * w,0.16))

print(gevoels_temperatuur)