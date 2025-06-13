def mult (matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in matrix A must match number of rows in matrix B")
    
    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    
    for i in range(len(matrix_a)):
        for j 