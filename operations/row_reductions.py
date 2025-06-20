from .row_operations import swap_rows, scale_row, add_rows

def row_echelon_form(matrix):
    m = [row[:] for row in matrix]  # Create a copy of the matrix to avoid modifying the original
    rows = len(m)
    cols = len(m[0]) if rows > 0 else 0
    pivot_row = 0
    for pivot_col in range(cols):
        found = False
        for r in range(pivot_row, rows): # Iterate over rows starting from the current pivot row
            if m[r][pivot_col] != 0:
                found = True
                swap_rows(m, pivot_row, r)
                break
        if not found: # No pivot found in this column
            continue
        pivot_value = m[pivot_row][pivot_col] 
        scale_row(m, pivot_row, 1 / pivot_value)  # Scale the pivot row to make the pivot value 1
        for r in range(pivot_row + 1, rows):
            factor = m[r][pivot_col]
            if factor != 0:
                add_rows(m, pivot_row, r, -factor) # Eliminate the entry below the pivot
        pivot_row += 1 # Move to the next pivot row
        if pivot_row >= rows:
            break
    return m

def reduced_row_echelon_form(matrix):
    m = row_echelon_form(matrix)  # Start with the row echelon form
    rows = len(m)
    cols = len(m[0])
    for pivot_row in range(rows - 1, -1, -1):  # Iterate from the last row to the first
        for 
