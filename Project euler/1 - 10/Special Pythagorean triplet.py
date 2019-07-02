prod = 0
till = 1000
for a in range(till):
    if prod != 0:
        break
    for b in range(a + 1, till):
        if prod != 0:
            break
        for c in range(b + 1, till):
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                if a + b + c == 1000:
                    prod = a * b * c

print(prod)