def longest_collatz_sequence(num):
    max_num = 0
    total, max_total = 1, 0
    while num != 1:
        total = 1
        n = num
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            total += 1
        if max_total < total:
            max_total = total
            max_num = num
        num -= 1
    return max_num


number = 1000000

print(longest_collatz_sequence(number))
