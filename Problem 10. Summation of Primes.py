def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        if i > int(num**0.5):
            break
    return True


def summation_or_primes(number):
    sum_primes = 0
    for i in range(2, number):
        if is_prime(i):
            sum_primes += i
    return sum_primes


print(summation_or_primes(int(input())))
