n = int(input())

for i in range(n):
    beide = input().split(' ')

    lengte = float(beide[0])
    gewicht = float(beide[1])

    bmi = gewicht / pow(lengte/100 , 2)

    print('{:.2f}'.format(bmi))
