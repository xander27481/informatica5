def vergeten_woorden(tekst, te_gebruiken):
    tekst = set(tekst.split(' '))
    lengte = len(te_gebruiken)
    woorden_in = len(tekst.intersection(te_gebruiken))
    return lengte, lengte - woorden_in, woorden_in


print(vergeten_woorden('hello world world world',{'python', 'piemel', 'hello', 'java'}))
print(vergeten_woorden('',{'python', 'world', 'hello', 'java'}))