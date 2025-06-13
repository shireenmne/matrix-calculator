from operations.matrix  import Matrix
from operations.add import add_matrices
from operations.subtract import sub_matrices

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])

result = add_matrices(a.data, b.data)
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Result of addition:")
print(Matrix(result))
result = sub_matrices(a.data, b.data)
print("Result of subtraction:")
print(Matrix(result))