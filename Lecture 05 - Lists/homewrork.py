###########################################################
# Number 4
###########################################################

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for row in range(len(matrix1)):
    for column in range(len(matrix1[0])):
        print(f"Row: {row}, Column: {column}")
        result[row][column] = matrix1[row][column] + matrix2[row][column]

for row in result:
    print(row)

###########################################################
# Number 5
###########################################################

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        result[column][row] = matrix[row][column]

for row in result:
    print(row)


###########################################################
# Number 6
###########################################################
import random

matrix = []

for row in range(4):
    nested_list = []
    for column in range(4):
        random_number = random.randint(1, 10)
        nested_list.append(random_number)
    else:
        matrix.append(nested_list)

for row in matrix:
    print(row)


comperhension_matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]

for row in comperhension_matrix:
    print(row)