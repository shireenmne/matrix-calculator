from .determinant import determinant
from .row_reductions import reduced_row_echelon_form

def inverse (matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Inverse can only be calculated for square matrices")
    if determinant(matrix)== 0:
        raise ValueError("Matrix is singular and cannot be inverted")
    augmented_matrix = [row + [1 if i == j else 0 for j in range(len(matrix))] for i, row in enumerate(matrix)]
    rref = reduced_row_echelon_form(augmented_matrix)
    inverse_matrix = [row[len(matrix):] for row in rref]
    return inverse_matrix