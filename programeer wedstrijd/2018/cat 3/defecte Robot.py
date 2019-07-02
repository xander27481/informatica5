aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    fout_lijn, correct_lijn = [], []
    fout_lijn += input()
    correct_lijn += input()
    print(fout_lijn)
    if fout_lijn == correct_lijn:
        fouten = 'correct'
    else:
        fouten = ''
        letter = ord('A')
        for i in range(len(fout_lijn)):
            if fout_lijn[i] != correct_lijn[i]:
                print(fout_lijn[i], correct_lijn[i])
                print(i)
                correctie = ''.join(fout_lijn).find(correct_lijn[i], i)
                print(correctie)
                fout_lijn[i], fout_lijn[correctie] = correct_lijn[i], fout_lijn[i]
                fouten += chr(letter + i) + chr(letter + correctie)
                print(fouten)
                print(''.join(fout_lijn) + '\n' + ''.join(correct_lijn))



        '''
        fouten = ''
        letter = ord('A')
        for i in range(len(fout_lijn)):
            if fout_lijn[i] != correct_lijn[i]: ##and fouten != 'onmogelijk':
                correctie = ''
                for a in range(i, len(fout_lijn)):
                    if fout_lijn[a] == correct_lijn[i]:# and correctie == '':
                        correctie = a
                if correctie != '':
                    fouten += chr(letter + i)
                    fouten += chr(letter + correctie)
                    fout_lijn = fout_lijn[:i] + fout_lijn[correctie] + fout_lijn[i + 1: correctie] + fout_lijn[i] + fout_lijn[correctie + 1:]
                else:
                    fouten = 'onmogelijk'
        '''

    #print(testgeval, fouten)