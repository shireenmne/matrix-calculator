
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
        if any(len(row) != self.cols for row in data):
            raise ValueError("All rows must have the same number of columns")
        
        