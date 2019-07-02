def vlag(richting, kleuren):
    output = ''
    if richting == 'verticaal':
        output = ' | '.join(kleuren)
    else:
        output = '\n-\n'.join(kleuren)
    return output.strip()

print(vlag('verticaal',('zwart', 'geel', 'rood')))
print(vlag('horizontaal',('rood', 'wit', 'blauw')))