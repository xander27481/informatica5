till = 100
sumA, sumB = 0, 0

for i in range(till + 1):
    sumA += i**2
    sumB += i

sumB = sumB**2
dif = max(sumA, sumB) - min(sumA, sumB)

print(dif)