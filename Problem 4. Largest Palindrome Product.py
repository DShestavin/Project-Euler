def largest_palindrome_product(number):
    max_number = 0
    for i in range(1, number):
        for j in range(1, number):
            k = i * j
            multiplier, max_multiplier = [], []
            while k > 0:
                multiplier.append(k % 10)
                k //= 10
            if (
                multiplier[0 : len(multiplier) // 2]
                == multiplier[: len(multiplier) // 2 - 1 : -1]
            ):
                for a in multiplier:
                    max_multiplier.append(str(a))
                max_multiplier = int("".join(max_multiplier))
                if max_number < max_multiplier:
                    max_number = max_multiplier
    return max_number


number = int(input())
print(largest_palindrome_product(number))
