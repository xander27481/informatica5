from math import pow, sqrt, pi
r = float(input('r: '))
v = float(input('v: '))
μ = 398600.4418 * pow(10,9)

a = (μ * r)/((2 * μ)-(r*pow(v, 2)))
p = 2 * pi * sqrt(pow(a, 3) / μ)

minuten = int((p//60) % 60)
uren = int(((p//60)//60) % 24)
dagen = int((((p // 60) // 60) // 24))

print('grote as:',str(a),'meter')
print('periode:',str(p),'seconden')
print('periode:',str(dagen),'dagen,',str(uren),'uren en',str(minuten),'minuten')