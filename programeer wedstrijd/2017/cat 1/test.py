dic = {}


for a in range(1,10):
    dic = {}
    dic['A'] = a
    lijst = [x for x in dic.values()]
    if len(lijst) == len(set(lijst)):
        for b in range(10):
            dic['B'] = b
            lijst = [x for x in dic.values()]
            if len(lijst) == len(set(lijst)):
                for c in range(10):
                    dic['C'] = c
                    lijst = [x for x in dic.values()]
                    if len(lijst) == len(set(lijst)):
                        for d in range(10):
                            dic['D'] = d
                            lijst = [x for x in dic.values()]
                            if len(lijst) == len(set(lijst)):
                                 print(dic)
                            else:
                                dic.pop('D')
                    else:
                        dic.pop('C')
            else:
                dic.pop('B')
