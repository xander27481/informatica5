def yiq(rgb):
    y_getallen, i_getallen, q_getallen = (0.299, 0.587, 0.114), (0.596, -0.274, -0.322), (0.211, -0.523, 0.312)

    y, i, q = 0, 0, 0

    for a in range(3):
        y, i, q = round(y + rgb[a] * y_getallen[a], 4), round(i + rgb[a] * i_getallen[a], 4), round(q + rgb[a] * q_getallen[a], 4)

    return y, i, q

print(yiq((82, 227, 112)))