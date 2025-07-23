def get_minor(matrix, row_to_remove, col_to_remove):
    return [row[:col_to_remove] + row[col_to_remove + 1:] for i, row in enumerate(matrix) if i != row_to_remove]

def determinant (matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Determinant can only be calculated for square matrices")
    
    if len(matrix) == 1:
        return matrix[0][0]
    
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    for col in range(len(matrix)):
        minor = get_minor(matrix, 0, col)
        cofactor = ((-1) ** col) * matrix[0][col] * determinant(minor)
        det += cofactor
    return det