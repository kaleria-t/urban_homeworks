numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
n = 0
is_prime = True
for i in numbers:
    for k in range(2, i):
        is_prime = (i % k)
        if is_prime == 0:
            not_primes.append(i)
            break
        elif is_prime != 0:
            n = n + 1
    if n == i - 2:
        primes.append(i)
    n = 0
print (primes)
print (not_primes)
