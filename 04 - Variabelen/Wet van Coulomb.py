Q1 = 2.0*(10**(-6))
Q2 = 1.0*(10**(-6))
r = (float(input('Afstand: ')))*10**(-2)
k0 = 8.99*(10**(9))

Fc = k0 * ((Q1 * Q2) / (r ** 2))

print(Fc)