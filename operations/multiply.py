def mult_matrices(matrix_a, matrix_b):
    # Check if matrices can be multiplied
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in matrix A must match number of rows in matrix B")
    
    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    
    for i in range(len(matrix_a)): # for each row in A
        for j in range(len(matrix_b[0])): # for each column in B
            for k in range(len(matrix_b)):  # loop over elements in row A and column B
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result            