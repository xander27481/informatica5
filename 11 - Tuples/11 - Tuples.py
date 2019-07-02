def yiq(tuple):
    y = (tuple[0] * 0.299) + (tuple[1] * 0.587) + (tuple[2] * 0.144)
    i = (tuple[0] * 0.596) + (tuple[1] * (-0.274)) + (tuple[2] * -0.322)
    q = (tuple[0] * 0.211) + (tuple[1] * (-0.523)) + (tuple[2] * 0.312)
    return y, i, q

print(yiq((255, 255, 255)))