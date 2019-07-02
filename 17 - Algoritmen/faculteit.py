def fac(n):
    if n ==1:
        return 1
    else:
        return n * fac(n - 1)

print(fac(4))

def palindroom(w):
    if len(w) == 1:
        return True
    else:
        return w[0] == w[-1] and palindroom(w[1: -1])

print(palindroom('lepel'))