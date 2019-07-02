primes = [2]
till = 10001
num = 1

while len(primes) != till:
    num += 2
    prime = True
    for i in primes:
        if num % i == 0:
            prime = False
            break
    if prime:
        primes.append(num)

print(primes[-1])