primes = [2]
till = 2000000
sum_ = 2

for num in range(3, till, 2):
    prime = True
    for i in primes:
        if num % i == 0:
            prime = False
            break
    if prime:
        sum_ += num
        primes.append(num)

print(sum_)