number = input()
rows = 19
for i in range(rows):
    number += input()

amount = 13
largest = 0
for i in range(0, len(number) - 13, 1):
    list = [int(number[i + x]) for x in range(amount)]
    prod = 1
    for a in list:
        prod *= a
    largest = max(largest, prod)

print(largest)