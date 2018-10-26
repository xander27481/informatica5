# input
temp = 0
warme_dagen = 0
hele_warme_dagen = 0
output = 'geen hittegolf'

temp = input('Wat is de temperatuur: ')

while temp != 'stop':
    if float(temp) >= 30:
        warme_dagen += 1
        hele_warme_dagen += 1
    elif float(temp) >= 25:
        warme_dagen += 1
    else:
        warme_dagen = hele_warme_dagen = 0
    if warme_dagen >= 5 and hele_warme_dagen >= 3:
        output = 'hittegolf'
    temp = input('Wat is de temperatuur: ')


if output == 'hittegolf':
    print('hittegolf')
else:
    print('geen hittegolf')