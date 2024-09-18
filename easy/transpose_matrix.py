def transposeMatrixMethodOne(matrix):
    height = len(matrix)
    width = len(matrix[0])

    res = [[0 for _ in range(height)] for _ in range(width)]

    for row in range(height):
        for col in range(width):
            res[col][row] = matrix[row][col]

    return res

def transposeMatrixMethodTwo(matrix):
    # Write your code here.
    res = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        res.append(newRow)
    return res
