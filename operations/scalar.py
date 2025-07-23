def scale_matrix (matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]