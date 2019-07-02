primes = [2]

# calculate all primes under 10000
for i in range(2,10000):
    prime = True
    for num in primes:
        if i % num == 0:
            prime = False
            break
    if prime:
        primes.append(i)

num = int(input('mooi: '))
max = 0

# calculate prime factors
for prime in primes:
    if num % prime == 0:
        num = num / prime
        max = prime

print(max)