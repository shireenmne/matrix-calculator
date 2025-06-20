def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return matrix

def scale_row(matrix, row, scalar):
    matrix[row] = [element * scalar for element in matrix[row]]
    return matrix

def add_rows(matrix, source_row, target_row, scalar=1):
    matrix[target_row] = [target_element + scalar * source_element for source_element, target_element in zip(matrix[source_row], matrix[target_row])]
    return matrix

