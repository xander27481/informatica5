from random import randint
from time import time
import matplotlib.pyplot as plt

def genereer_rij(a):
    rij = []
    for i in range(a):
        rij.append(randint(0, a))
    return rij

def binairy_search(lijst, low, high, getal):
    if high < low:
        return False
    mid = (low + high) // 2
    if lijst[mid] == getal:
        return True
    elif getal < lijst[mid]:
        return binairy_search(lijst, low, mid - 1, getal)
    elif lijst[mid] < getal:
        return binairy_search(lijst, mid + 1, high, getal)


def linear_search(lijst, getal):
    index = 0
    while index < len(lijst) and lijst[index] != getal:
        index += 1
    return index < len(lijst)

'''
lijst = [2, 3, 5, 7, 8, 10, 12, 15, 18, 20]
print(binairy_search(lijst, 0, len(lijst) - 1, int(input('welk getal? '))))
'''

##### werkt niet #####
n, t_bs, t_ls = [], [], []
i = 10

while i < 10000:
    rij_1 = genereer_rij(20)
    rij_1.sort()
    rij_2 = rij_1.copy()
    getal = randint(0, i)

    start = time()
    binairy_search(rij_1, 0, len(rij_1) - 1, getal)
    stop = time()
    t_bs.append(stop - start)

    start = time()
    linear_search(rij_2, getal)
    stop = time()
    t_ls.append(stop - start)

    n.append(i)
    i += 50

plt.plot(n, t_ls)
plt.plot(n, t_bs)
plt.gca().legend(('linear search', 'binary search'))
plt.show()