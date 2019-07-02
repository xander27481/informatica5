till = 20
num = 0
smallest = 0

while smallest == 0:
    num += 2
    jah = True
    for i in range(2, till):
        if num % i != 0:
            jah = False
    if jah:
        smallest = num

print(smallest)