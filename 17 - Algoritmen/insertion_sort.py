from random import randint
from time import time
import matplotlib.pyplot as plt

def insertion_sort(a):
    for j in range(1, len(a)):
        key =  a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

    return a

def  bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1]  = a[j - 1],  a[j]

    return a

def other_sort(a):
    pass

def merg(l1, l2):
    lijst = []
    index1, index2 = 0, 0

    while index1 < len(l1) and index2 < len(l2):
        if l1[index1] <= l2[index2]:
            lijst.append(l1[index1])
            index1 += 1
        elif l1[index1] > l2[index2]:
            lijst.append(l2[index2])
            index2 += 1

    lijst += l1[index1:] + l2[index2:]

    return lijst

def merge_sort(lijst):
    if len(lijst) > 1:
        mid = len(lijst) // 2
        s1 = merge_sort(lijst[:mid])
        s2 = merge_sort(lijst[mid:])
        return merg(s1, s2)
    else:
        return lijst

def genereer_rij(a):
    rij = []
    for i in range(a):
        rij.append(randint(0, a))
    return rij

n, t_insertion, t_python, t_bubble, t_merge = [], [], [], [], []

i = 10

while i < 100:

    rij_1 = genereer_rij(i)
    rij_2 = rij_1.copy()
    rij_3 = rij_1.copy()
    rij_4 = rij_1.copy()

    start = time()
    insertion_sort(rij_1)
    stop = time()

    t_insertion.append(stop - start)

    start = time()
    rij_2.sort()
    stop = time()

    t_python.append(stop - start)

    start = time()
    bubble_sort(rij_3)
    stop = time()

    t_bubble.append(stop - start)

    """
    start = time()
    merge_sort(rij_4)
    stop = time()

    t_merge.append(stop - start)
    """

    n.append(i)
    i += 50

plt.plot(n, t_insertion, '-rs')
plt.plot(n, t_python, '-bd')
plt.plot(n, t_bubble, '-go')
#plt.plot(n, t_merge, '-yo')
plt.xlabel('Aantal')
plt.ylabel('Tijd')
plt.gca().legend(('Insertion sort', 'Python sort', 'Bubble sort', 'Merge sort'))
plt.gcf().canvas.set_window_title('EEN HEEL MOOI DING JONGE')
plt.title('ZO MOOI DING')
plt.show()
