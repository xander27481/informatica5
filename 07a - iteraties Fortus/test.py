lievelings_fruit = input('geef je lievelings fruit: ')
m = 'm'
for letter in lievelings_fruit:
    print(letter + m)
    m += m

print('\n')

for i in range(10):
    print(i)

for i in range(0, 1001, 100):
    #        start, stop, stap -> allemaal int (-step -> start > stop)
    print(i)