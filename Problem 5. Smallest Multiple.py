def smallest_multiple(number):
    check = True
    number_multiple = number
    while check:
        total = 0
        number_multiple += 1
        for i in range(1, number + 1):
            if number_multiple % i == 0:
                total += 1
            else:
                break
        if total == number:
            check = False
    return number_multiple


print("Введите количество делителей:")
number = int(input())
print(smallest_multiple(number))
