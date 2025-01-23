def sum_square_difference(number):
    sum_squares, squares_sum = 0, 0
    for i in range(1, number + 1):
        sum_squares += i**2
        squares_sum += i
    return squares_sum**2 - sum_squares


number = int(input())
print(sum_square_difference(number))
