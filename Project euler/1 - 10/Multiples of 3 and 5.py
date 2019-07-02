sum = 0

till = int(input())
for i in range(till):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)