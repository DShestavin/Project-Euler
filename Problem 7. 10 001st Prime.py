def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def sum_square_difference(number):
    total, num = 0, 1
    while total != number:
        num += 1
        if is_prime(num):
            total += 1
    return num


number = int(input())
print(sum_square_difference(number))
