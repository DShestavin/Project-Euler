def highly_divisible_triangular_number(devisor_number):
    triangle_number, triangle_number_0 = 1, 1
    total_divisors = 1

    while total_divisors < devisor_number:
        total_divisors = 0
        triangle_number += triangle_number_0 + 1
        triangle_number_0 += 1
        for i in range(1, int(triangle_number**0.5) + 1):
            if triangle_number % i == 0:
                total_divisors += 1
        total_divisors *= 2

    return triangle_number


devisor_number = 500

print(highly_divisible_triangular_number(devisor_number))
