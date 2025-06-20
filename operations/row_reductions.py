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
        if pivot_value != 1:
            scale_row(m, pivot_row, 1 / pivot_value) # Normalize the pivot row
        for r in range(pivot_row + 1, rows):
            factor = m[r][pivot_col]
            if factor != 0:
                add_rows(m, pivot_row, r, -factor) # Eliminate the entry below the pivot
        pivot_row += 1 # Move to the next pivot row
        if pivot_row >= rows:
            break
    return m

def reduced_row_echelon_form(matrix):

        

