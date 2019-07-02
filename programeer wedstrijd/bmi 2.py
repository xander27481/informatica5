n = int(input())
output = ''
lengtes = input().split(' ')
gewichten = input().split(' ')

for i in range(n):
    output += (str(round(int(gewichten[i]) / pow(int(lengtes[i]) / 100, 2), 2)) + ' ')

print(output)


#### of ####


n = int(input())

lengtes = input().split(' ')
gewichten = input().split(' ')

for i in range(n):
    print(str(round(int(gewichten[i]) / pow(int(lengtes[i]) / 100, 2), 2)), end=' ')

print()