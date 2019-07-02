peer = ['zap', 'zip', 'zop', 'zup', 'zep']
jap = [1, 2, 3, 4, 5]

new = zip(peer, jap)

with open('oh.txt', 'a') as bestand:
    bestand.write('\n'.join(new))