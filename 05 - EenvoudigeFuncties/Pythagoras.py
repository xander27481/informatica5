from math import sqrt

a = float(input('eerste zijde: '))
b = float(input('tweede zijde: '))

c = sqrt(pow(a,2) + pow(b,2))

print('In een rechthoekige driekhoek met rechthoekzijden a =','{:2.2f}'.format(a),'en b =','{:2.2f}'.format(b),'is de schuine zijde','{:2.2f}'.format(c))