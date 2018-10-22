# input
aantal_lifters = int(input('Hoeveel lifters zijn er: '))
max = 0
max_i = 0

for i in range(1 , aantal_lifters + 1):
    score = float(input('Geef de score: '))
    if i <= aantal_lifters // 2:
        if score > max:
            max = score
    elif i == aantal_lifters and max_i == 0:
        max = score
    elif i > aantal_lifters // 2:
        if score > max and max_i == 0:
            max = score
            max_i = 1

print(max)