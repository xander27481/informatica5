a = int(input('getal 1: '))
b = int(input('getal 2: '))

i = 0
print('{:>6d}'.format(a * pow(10,i)),'+','{:<6d}'.format(b * pow(10,i)),'=',str((a * pow(10,i)) + (b * pow(10,i))))
i += 1
print('{:>6d}'.format(a * pow(10,i)),'+','{:<6d}'.format(b * pow(10,i)),'=',str((a * pow(10,i)) + (b * pow(10,i))))
i += 1
print('{:>6d}'.format(a * pow(10,i)),'+','{:<6d}'.format(b * pow(10,i)),'=',str((a * pow(10,i)) + (b * pow(10,i))))
i += 1
print('{:>6d}'.format(a * pow(10,i)),'+','{:<6d}'.format(b * pow(10,i)),'=',str((a * pow(10,i)) + (b * pow(10,i))))
i += 1
print('{:>6d}'.format(a * pow(10,i)),'+','{:<6d}'.format(b * pow(10,i)),'=',str((a * pow(10,i)) + (b * pow(10,i))))


print('{:>6d} + {:<6d} = {:d}'.format(a * pow(10,i),b * pow(10,i),(a * pow(10,i)) + (b * pow(10,i))))