def sub_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return result
