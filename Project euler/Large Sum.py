sum = 0
lijn = int(input())
while lijn != '':
    sum += int(lijn)
    lijn = str(input())

print(sum)
print(str(sum)[0:10])