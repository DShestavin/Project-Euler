def largest_product_in_a_series(number):
    list_number = list()
    max_piece = 0
    for i in number:
        list_number.append(int(i))
    for i in range(988):
        piece = 1
        for j in range(i, i + 13):
            piece *= list_number[j]
        if max_piece < piece:
            max_piece = piece
    return max_piece


number = input()
print(largest_product_in_a_series(number))
