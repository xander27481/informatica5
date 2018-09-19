# berekent de discriminant
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
discriminant = int(b**2 - 4 * a * c)
print(discriminant)

x1 = ((b*-1)+(discriminant ** (1/2))) / a * 2
x2 = ((b*-1)+(discriminant ** (1/2))) / a * 2

print(x1, x2)