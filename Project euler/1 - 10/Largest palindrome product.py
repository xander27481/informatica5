largest = 0

for a in range(100,1000):
    for b in range(100, 1000):
        num = a * b
        if str(num) == str(num)[::-1]:
            largest = max(num, largest)

print(largest)