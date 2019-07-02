def maal_deel(rekenslang):
    slang = []
    vorige = ''
    for i in range(len(rekenslang) - 1):
        if rekenslang[i] not in bewerkingen and rekenslang[i + 1] not in ('*', ':') and vorige not in ('*', ':'):
            slang.append(rekenslang[i])
            vorige = ''
        elif rekenslang[i] not in bewerkingen and rekenslang[i + 1] in ('*', ':') and vorige not in ('*', ':') and rekenslang[i - 1] == ':':
            slang.append(rekenslang[i])
        elif rekenslang[i] not in bewerkingen and rekenslang[i + 1] in ('*', ':') and vorige not in ('*', ':'):
            vorige = rekenslang[i]
        elif rekenslang[i] not in bewerkingen:
            vorige = ''

        elif rekenslang[i] in ('+', '-'):
            slang.append(rekenslang[i])
            vorige = ''
        elif rekenslang[i] == '*' and vorige not in ('*', ':') and not vorige == '':
            slang.append(int(vorige) * int(rekenslang[i + 1]))
            vorige = '*'
        elif rekenslang[i] == ':' and vorige not in ('*', ':') and not vorige == '':
            slang.append(int(vorige) / int(rekenslang[i + 1]))
            vorige = ':'
        else:
            slang.append(rekenslang[i])
    if rekenslang[-2] not in ('*', ':'):
        slang.append(rekenslang[-1])
    elif rekenslang[-2] in ('*', ':') and rekenslang[-4] in ('*', ':'):
        slang.append(rekenslang[-1])
    #print(rekenslang)
    return slang


def som_verschil(rekenslang):
    slang = []
    vorige = rekenslang[0]
    for i in range(1, len(rekenslang)):
        if rekenslang[i] == '+' and vorige != '+':
            slang.append(int(vorige) + int(rekenslang[i + 1]))
            vorige = '+'
        elif rekenslang[i] == '+':
            slang.append(rekenslang[i])
            vorige = ''
        elif vorige != '+' and i == len(rekenslang) - 1:
            slang.append(rekenslang[i])
        elif vorige != '+':
            vorige = rekenslang[i]
    #print(slang)
    return slang


def letters_check(letters, rekenslang):
    a, rekenslang = rekenslang, ''
    for element in a:
        if str(element) in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            rekenslang += str(letters[element]) + ' '
        else:
            rekenslang += str(element) + ' '

    rekenslang = rekenslang.split(' ')[:-1]
    #print(rekenslang)
    return rekenslang


def min_check(rekenslang):
    a, rekenslang, vorige = rekenslang, '', ''
    for element in a:
        if element not in ('+', '-'):
            if vorige == '-':
                rekenslang += str(-int(element)) + ' '
            else:
                rekenslang += str(int(element)) + ' '
            vorige = ''
        elif element == '+':
            rekenslang += str(element) + ' '
        else:
            rekenslang += '+' + ' '
            vorige = '-'
    rekenslang = rekenslang.split(' ')[:-1]
    #print(rekenslang)
    return rekenslang


def oplossen(letters, rekenslang):
    rekenslang = letters_check(letters, rekenslang)

    while '*' in rekenslang or ':' in rekenslang:
        rekenslang = maal_deel(rekenslang)

    rekenslang = min_check(rekenslang)

    while '+' in rekenslang:
        rekenslang = som_verschil(rekenslang)

    #print(rekenslang)
    if int(rekenslang[0]) == uitkomst:
        return  letters


aantal_testgevallen = int(input())

bewerkingen = ('+', '-', '*', ':')

for testgeval in range(1, aantal_testgevallen + 1):
    getalen = [int(i) for i in input().split(' ')]
    info = input().split(' ')
    rekenslang = info[:-2]
    #print(rekenslang)
    backup = rekenslang
    uitkomst = int(info[-1])
    '''
    if len(getalen) == 1:
        for a in getalen:
            letters['A'] = a

            rekenslang = letters_check(letters, rekenslang)
            #print('na letter check:',rekenslang)

            while '*' in rekenslang or ':' in rekenslang:
                rekenslang = maal_deel(rekenslang)

            rekenslang = min_check(rekenslang)
            #print('na min check:',rekenslang)

            while '+' in rekenslang:
                rekenslang = som_verschil(rekenslang)

            if int(rekenslang[0]) == uitkomst:
                print('{} A={}'.format(testgeval, letters['A']))

    if len(getalen) == 2:
        for a in getalen:
            letters['A'] = a
            for b in getalen:
                letters['B'] = b
                rekenslang = backup
                oplossen(letters, rekenslang)
    '''
    for a in getalen:
        letters = {}
        letters['A'] = a
        lijst = [x for x in letters.values()]
        if len(lijst) == len(set(lijst)) and len(getalen) == 1:

            letters = oplossen(letters, rekenslang)
            print('{} A={}'.format(testgeval, letters['A']))

        else:

            for b in getalen:
                letters['B'] = b
                lijst = [x for x in letters.values()]
                if len(lijst) == len(set(lijst)) and len(getalen) == 2:

                    output = oplossen(letters, rekenslang)
                    if output != None:
                        print('{} A={} B={}'.format(testgeval, letters['A'], letters['B']))

                elif len(lijst) == len(set(lijst)):

                    for c in getalen:
                        letters['C'] = c
                        lijst = [x for x in letters.values()]
                        if len(lijst) == len(set(lijst)) and len(getalen) == 3:

                            output = oplossen(letters, rekenslang)
                            if output != None:
                                print('{} A={} B={} C={}'.format(testgeval, letters['A'], letters['B'], letters['C']))

                        elif len(lijst) == len(set(lijst)):

                            for d in getalen:
                                letters['D'] = d
                                lijst = [x for x in letters.values()]
                                if len(lijst) == len(set(lijst)) and len(getalen) == 4:

                                    output = oplossen(letters, rekenslang)
                                    if output != None:
                                        print('{} A={} B={} C={} D={}'.format(testgeval, letters['A'], letters['B'], letters['C'], letters['D']))

                                elif len(lijst) == len(set(lijst)):

                                    for e in getalen:
                                        letters['E'] = e
                                        lijst = [x for x in letters.values()]
                                        if len(lijst) == len(set(lijst)) and len(getalen) == 5:

                                            output = oplossen(letters, rekenslang)
                                            if output != None:
                                                print('{} A={} B={} C={} D={} E={}'.format(testgeval,letters['A'], letters['B'], letters['C'], letters['D'], letters['E']))

                                        elif len(lijst) == len(set(lijst)):

                                            for f in getalen:
                                                letters['F'] = f
                                                lijst = [x for x in letters.values()]
                                                if len(lijst) == len(set(lijst)) and len(getalen) == 6:

                                                    output = oplossen(letters, rekenslang)
                                                    if output != None:
                                                        print('{} A={} B={} C={} D={} E={} F={}'.format(testgeval, letters['A'], letters['B'], letters['C'], letters['D'], letters['E'], letters['F']))

                                                elif len(lijst) == len(set(lijst)):

                                                    for g in getalen:
                                                        letters['G'] = g
                                                        lijst = [x for x in letters.values()]
                                                        if len(lijst) == len(set(lijst)) and len(getalen) == 7:

                                                            output = oplossen(letters, rekenslang)
                                                            if output != None:
                                                                print('{} A={} B={} C={} D={} E={} F={} G={}'.format( testgeval, letters['A'], letters['B'], letters['C'], letters['D'], letters['E'], letters['F'], letters['G']))

                                                        elif len(lijst) == len(set(lijst)):

                                                            for h in getalen:
                                                                letters['H'] = h
                                                                lijst = [x for x in letters.values()]
                                                                if len(lijst) == len(set(lijst)) and len(getalen) == 8:

                                                                    output = oplossen(letters, rekenslang)
                                                                    if output != None:
                                                                        print('{} A={} B={} C={} D={} E={} F={} G={} H={}'.format( testgeval, letters['A'], letters['B'], letters['C'], letters['D'], letters['E'], letters['F'], letters['G'], letters['H']))

                                                                elif len(lijst) == len(set(lijst)):

                                                                    for i in getalen:
                                                                        letters['I'] = i
                                                                        lijst = [x for x in letters.values()]
                                                                        if len(lijst) == len(set(lijst)) and len(getalen) == 9:

                                                                            output = oplossen(letters, rekenslang)
                                                                            if output != None:
                                                                                print('{} A={} B={} C={} D={} E={} F={} G={} H={} I={}'.format(testgeval, letters['A'], letters['B'], letters['C'], letters['D'], letters['E'], letters['F'], letters['G'], letters['H'], letters['I']))

                                                                        letters.pop('I')
                                                                letters.pop('H')
                                                        letters.pop('G')
                                                letters.pop('F')
                                        letters.pop('E')
                                letters.pop('D')
                        letters.pop('C')
                letters.pop('B')




# 1
# 7
# 19 * 10 + 22 * 16 - 6 - 15 + 24 : 4 + 8 * 17 * 11 + 18 * 3 + 13 + A * 25 + 14 * 1 - 2 * 12 * 23 + 20 + 21 * 7 - 5 = 1889