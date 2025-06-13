from .add import add_matrices
from .subtract import sub_matrices
from .multiply import mult_matrices
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