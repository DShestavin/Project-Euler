def largest_product_in_a_grid(matrix):
    creations = list()

    for i in range(len(matrix)):  # нахождение всех произведений по горизонтали
        for j in range(len(matrix[i]) - 3):
            proizvedenie = 1
            for k in range(4):
                proizvedenie *= int(matrix[i][j + k])
            creations.append(proizvedenie)

    for i in range(len(matrix) - 3):  # нахождение всех произведений по вертикали
        for j in range(len(matrix[i])):
            proizvedenie = 1
            for k in range(4):
                proizvedenie *= int(matrix[i + k][j])
            creations.append(proizvedenie)

    for i in range(len(matrix) - 3):  # нахождение всех произведений по диагонали слева
        for j in range(len(matrix[i]) - 3):
            proizvedenie = 1
            for k in range(4):
                proizvedenie *= int(matrix[i + k][j + k])
            creations.append(proizvedenie)

    for i in range(3, len(matrix)):  # нахождение всех произведений по диагонали справа
        for j in range(len(matrix[i]) - 3):
            proizvedenie = 1
            for k in range(4):
                proizvedenie *= int(matrix[i - k][j + k])
            creations.append(proizvedenie)

    return max(creations)


matrix = [input().split() for _ in range(20)]  # создем матрицу 20х20

print(largest_product_in_a_grid(matrix))
