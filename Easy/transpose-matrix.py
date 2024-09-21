# Problem : https://www.algoexpert.io/questions/transpose-matrix


def transposeMatrix(matrix):
    """
    Creates a new matrix with transposed rows and columns.

    Thought Process:
    1. Determine the height (`m`) and width (`n`) of the input matrix.
    2. Create a result matrix (`res`) of size `n x m` filled with zeroes.
    3. Iterate through each element of the input matrix.
    4. Assign each element to its corresponding transposed position in the result matrix:
       - Element at position (row, col) in the input becomes (col, row) in the result.
    5. Return the result matrix.

    Time Complexity: O(m * n), where `m` is the number of rows and `n` is the number of columns.
    Space Complexity: O(m * n) for the new transposed matrix.
    """
    height = len(matrix)
    width = len(matrix[0])

    res = [[0 for _ in range(height)] for _ in range(width)]

    for row in range(height):
        for col in range(width):
            res[col][row] = matrix[row][col]

    return res


def transposeMatrix(matrix):
    """
    Constructs the transposed matrix by building new rows.

    Thought Process:
    1. Initialize an empty list (`res`) to hold the rows of the transposed matrix.
    2. Iterate over each column index in the original matrix:
       - Create a new row for the transposed matrix.
       - For each column index, iterate through each row index and collect the elements.
       - Append the newly formed row to the result matrix.
    3. Return the result matrix.

    Time Complexity: O(m * n) because each element is accessed once.
    Space Complexity: O(m * n) for the new transposed matrix.
    """
    res = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        res.append(newRow)
    return res