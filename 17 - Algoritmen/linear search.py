def linear_search(lijst, getal):
    index = 0

    while index < len(lijst) and lijst[index] != getal:
        index += 1
    return index < len(lijst)

lijst = [2, 3, 5, 7, 8, 10, 12, 15, 18, 20]
print(linear_search(lijst, int(input('welk getal? '))))
