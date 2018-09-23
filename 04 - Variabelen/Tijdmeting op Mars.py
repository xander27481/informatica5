sol = int(input('aantal sol: '))

seconden = int((sol * 35.244) % 60)
minuten = int(((sol * 39) + ((sol * 35.244) // 60)) % 60)
uren = int(((sol * 24) + (((sol * 39) + (sol * 35.244) // 60) // 60)) % 24)
dagen = int(((sol * 24) + (((sol * 39) + (sol * 35.244) // 60) // 60)) // 24)

print(sol,'sol =',dagen,'dagen,',uren,'uren,',minuten,'minuten en',seconden,'seconden')
