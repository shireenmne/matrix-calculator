from .add import add_matrices
from .subtract import sub_matrices
from .multiply import mult_matrices
from .row_operations import swap_rows, scale_row, add_rows
from .row_reductions import row_echelon_form, reduced_row_echelon_form
from .transpose import transpose

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
        if any(len(row) != self.cols for row in data):
            raise ValueError("All rows must have the same number of columns")
        
    def __str__(self):
        row_strings=[]
        for row in self.data:
            str_elements = []
            for element in row:
                str_elements.append(str(element))
            row_string = '\t'.join(str_elements)
            row_strings.append(row_string)
            matrix_string = '\n'.join(row_strings)
        return matrix_string
    
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only add another Matrix instance")
        result = add_matrices(self.data, other.data)
        return Matrix(result)
    
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract another Matrix instance")
        result = sub_matrices(self.data, other.data)
        return Matrix(result)
    
    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only multiply by another Matrix instance")
        result = mult_matrices(self.data, other.data)
        return Matrix(result)
    
    def swap_rows(self, row1, row2):
        if row1 < 0 or row2 < 0 or row1 >= self.rows or row2 >= self.rows:
            raise IndexError("Row indices out of range")
        swap_rows(self.data, row1, row2)
        return self
    
    def scale_row(self, row, scalar):
        if row < 0 or row >= self.rows:
            raise IndexError("Row index out of range")
        scale_row(self.data, row, scalar)
        return self
    
    def add_rows(self, source_row, target_row, scalar=1):
        if source_row < 0 or target_row < 0 or source_row >= self.rows or target_row >= self.rows:
            raise IndexError("Row indices out of range")
        add_rows(self.data, source_row, target_row, scalar)
        return self
    
    def transpose(self):
        result = transpose(self.data)
        return Matrix(result)
    
    def row_echelon_form(self):
        result = row_echelon_form(self.data)
        return Matrix(result)
    
    def reduced_row_echelon_form(self):
        results = reduced_row_echelon_form(self.data)
        return Matrix(results)