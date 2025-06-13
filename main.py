from operations.matrix  import Matrix
from operations.add import add_matrices
from operations.subtract import sub_matrices
from operations.matrix import Matrix

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("A + B:")
print(a + b)
print("A - B:")
print(a - b)
print("A * B:")
print(a * b)