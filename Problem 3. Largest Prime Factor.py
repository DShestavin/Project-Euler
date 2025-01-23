def largest_prime_factor(number):
    all_divisors, all_simple_divisors = list(), list()
    for i in range(2, int(number**0.5)):
        if number % i == 0:
            all_divisors.append(i)
    for i in all_divisors:
        total = 0
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                total += 1
                if total > 2:
                    break
        if total == 0:
            all_simple_divisors.append(i)
    return max(all_simple_divisors)


print(largest_prime_factor(600851475143))
