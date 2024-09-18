def transposeMatrix(matrix):
    height = len(matrix)
    width = len(matrix[0])

    res = [[0 for _ in range(height)] for _ in range(width)]

    for row in range(height):
        for col in range(width):
            res[col][row] = matrix[row][col]

    return res