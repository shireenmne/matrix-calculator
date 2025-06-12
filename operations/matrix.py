
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
            row_strings = '\t'.join(str_elements)
            row_strings.append(row_strings)
            matrix_string = '\n'.join(row_strings)
        return matrix_string