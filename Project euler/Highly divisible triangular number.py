till = 20000

getal = 0

primes = [2]
num = 1

while len(primes) != till / 4:
    num += 2
    prime = True
    for i in primes:
        if num % i == 0:
            prime = False
            break
    if prime:
        primes.append(num)

primes = [1] + primes
print(primes)
input()

for i in range(1, till + 1):
    getal += i
    delers = set()
    a = 0
    prime = primes[a]
    if getal % prime == 0:
        delers.add(prime)
        delers.add(getal / prime)
    a += a
    while prime < getal // 2 and a < len(primes):
        prime = primes[a]
        if getal % prime == 0:
            delers.add(prime)
            delers.add(getal / prime)
        a += 1

    if i % 100 == 0:
        print('i', i)
        print('getal', getal)
        print('delers', delers)
        print('len', len(delers))

    if len(delers) > 500:
        print(getal)
        break