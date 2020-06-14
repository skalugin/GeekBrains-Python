class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        pass

    def __add__(self, other):
        matrix_1 = self.matrix
        matrix_2 = other.matrix
        res = []
        for i in range(len(matrix_1)):
            row = []
            for j in range(len(matrix_1[0])):
                row.append(matrix_1[i][j] + matrix_2[i][j])
            res.append(row)
        self.matrix = res
        #return res

    def __str__(self):
        matrix = ''
        for row in self.matrix:
            matrix = matrix + ' '.join(str(row)) + '\n'
        return matrix



matrix_1 = Matrix([[1, 2, 3],
                  [2, 3, 4],
                  [3, 4, 5]])
matrix_2 = Matrix([[4, 5, 6],
                  [5, 6, 7],
                  [6, 7, 8]])

matrix_1 + matrix_2
print(matrix_1)