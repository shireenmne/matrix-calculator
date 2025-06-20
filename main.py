from operations.matrix  import Matrix
from operations.row_reductions import row_echelon_form


a = Matrix([[1, 2], [3, 4], [5, 6]])
b = Matrix([[5, 6], [7, 8]])
print("Matrix A:")
print(a)
print(row_echelon_form(a.data))