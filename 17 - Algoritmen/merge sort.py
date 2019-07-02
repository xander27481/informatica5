l1 = [2, 4, 6]
l2 = [3, 5, 7]

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

    '''
    if index1 < len(l1):
        lijst += l1[index1:]
    else:
        lijst += l2[index2:]
    '''
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

print(merg(l1, l2))

print(merge_sort([9,5,7,3,5,1,7,4]))