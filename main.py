
class MatrixProduct:
    def product(self, array, rows, column, b):

        for i in range(rows):
            for j in range(column):
                array[i][j] *= b

        return array
rows = int(input())
column = int(input())
array = []
b = int(input())
for i in range(rows):
    a = list(map(int, input().split()))
    array.append(a)

object = MatrixProduct()
print(object.product(array, rows, column, b))

