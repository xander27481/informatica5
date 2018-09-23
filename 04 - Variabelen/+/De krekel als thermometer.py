N60 = int(input('minuten: '))

Tf = 50 + ((N60 - 40) / 4)
Tc = 10 + ((N60 - 40) / 7)

print('temperatuur (Fahrenheit):', Tf)
print('temperatuur (Celsius):', Tc)