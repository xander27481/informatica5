def lees_aandeel(file_name):
    output = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            new = line.split(';')
            new[-1] = ''.join(new[-1].split(',')).strip()
            output.append(new)
    return output

def selecteer_kolom(info, file_name):
    file = lees_aandeel(file_name)
    kolom = 0
    for element in file[0]:
        if element == info:
            info = kolom
        kolom += 1
    output = []
    for line in file[1:]:
        cijfer = float(line[info])
        if str(cijfer)[-2:] == '.0':
            cijfer = int(cijfer)
        output.append(cijfer)
    return output

def hoogste_koers(lijst):
    hoogste = 0
    for element in lijst:
        try:
            if element > hoogste:
                hoogste = element
        except:
            pass
    return hoogste

print(lees_aandeel('Apple.txt'))
print(selecteer_kolom('Close','Apple.txt'))

print(hoogste_koers([3, 'AAAAAA', 6, 7, 99999, 999]))