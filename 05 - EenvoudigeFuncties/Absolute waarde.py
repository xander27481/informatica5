x = float(input('x: '))
y = float(input('y: '))

uit1 = abs(abs(x) - abs(y))
uit2 = abs(x-y)

print('{:6.4f}'.format(uit1),'\N{LESS-THAN OR EQUAL TO}','{:6.4f}'.format(uit2))