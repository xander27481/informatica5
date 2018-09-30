from math import pi,pow
r = float(input('r: '))
R = float(input('R: '))

n = int(0.83*(pow(R,2)/pow(r,2))-1.9)
bedekking = ((pow(r,2)*pi*n)/(pow(R,2)*pi))*100

print(str(n),'kleine cirkels bedekken','{:4.2f}'.format(bedekking) + '%','van de grote cirkel')