path = 'output_slang.txt'
check = 'check_slang.txt'

code = open(path, 'r')
check = open(check, 'r')

for i in range(len(code.readlines())):
    if code.readline(i) == check.readline(i):
        print(code.readline(i), check.readline(i))