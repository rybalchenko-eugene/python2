# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def rev_matrix(array: list[list[int]]) -> list[int]:
    res_matrix = []

    for row in range(0, len(array[0])):
        row_arr = []
        for line in array:
            row_arr.append(line[row])
        yield row_arr


matrix = [[2, 4, 7], [3, 8, 3], [4, 45, 3], [5, 18, 22]]
print(matrix)
print(*rev_matrix(matrix))

