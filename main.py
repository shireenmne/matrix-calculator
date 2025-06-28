from operations.matrix  import Matrix


m = Matrix([
    [1, 2, -1, -4],
    [2, 3, -1, -11],
    [-2, 0, -3, 22]
])

print("Original Matrix:")
print(m)

rref = m.reduced_row_echelon_form()

print("\nReduced Row Echelon Form:")
print(rref)
