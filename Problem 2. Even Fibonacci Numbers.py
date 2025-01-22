def sum_of_even_febonachi(number):
    febonachi_1, febonachi_2 = 0, 1
    febonachi_n, sum_febonachi = int(), int()
    while febonachi_n < number:
        febonachi_n = febonachi_1 + febonachi_2
        febonachi_1 = febonachi_2
        febonachi_2 = febonachi_n
        if febonachi_n % 2 == 0:
            sum_febonachi += febonachi_n
    return sum_febonachi


print(sum_of_even_febonachi(4000000))
