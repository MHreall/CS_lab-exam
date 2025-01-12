def find_matrix_shape(matrix):
    if not matrix:  
        return (0, 0)
    row = len(matrix)
    column = len(matrix[0]) if isinstance(matrix[0], list) else 0
    return (row, column)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(find_matrix_shape(matrix))  

