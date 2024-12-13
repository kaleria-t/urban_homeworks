def is_prime(func):
    def wrapper(*args):
        prime_count = 0
        res = func(*args)
        for n in range(2, res):
            if res % n == 0:
                prime_count += 1
                return 'Составное'
        if prime_count == 0:
            return 'Простое'
    return wrapper
@is_prime
def sum_three(a, b, c):
    print(a+b+c)
    return a+b+c
result = sum_three(2, 3, 6)
print(result)