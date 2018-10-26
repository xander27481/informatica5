# input
num = int(input('Wat is het serie nummer: '))
m = num
n = 0

while num >= 0:
    n += 1
    num = int(input('Wat is het serie nummer: '))
    m = max(m, num)

t = round((((n + 1) * m) / n) - 1)

print('Het aantal geproduceerde tanks wordt geschat op {}.'.format(t))
