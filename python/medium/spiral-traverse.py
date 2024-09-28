# Problem : https://www.algoexpert.io/questions/spiral-traverse

def spiralTraverse(array):
    """
    Thought Process:
    The goal is to traverse a 2D array in a spiral order and return the elements in that order.

    Approach:
    1. We need to traverse the array layer by layer, starting from the outermost elements and spiraling inward.
    2. Initialize four boundaries:
       - `top`: The first row that hasn't been traversed.
       - `bottom`: The last row that hasn't been traversed.
       - `left`: The first column that hasn't been traversed.
       - `right`: The last column that hasn't been traversed.
    3. While the boundaries don't overlap (i.e., `top <= bottom` and `left <= right`), we proceed with the following steps:
       - Traverse from left to right across the top row and increment the `top` boundary.
       - Traverse from top to bottom down the rightmost column and decrement the `right` boundary.
       - Traverse from right to left across the bottom row and decrement the `bottom` boundary.
       - Traverse from bottom to top up the leftmost column and increment the `left` boundary.
    4. After each step, check if the updated boundaries still satisfy the condition for further traversal (`top <= bottom` and `left <= right`).
    5. Continue until all elements have been traversed, and return the result list.

    Time Complexity: O(n), where n is the total number of elements in the array, since each element is visited exactly once.
    """
    if not array:
        return []

    top = 0
    bottom = len(array) - 1
    left = 0
    right = len(array[0]) - 1
    res = []

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res.append(array[top][i])
        top += 1

        if top > bottom:
            break

        for i in range(top, bottom + 1):
            res.append(array[i][right])
        right -= 1

        if left > right:
            break

        for i in range(right, left - 1, -1):
            res.append(array[bottom][i])
        bottom -= 1

        if top > bottom:
            break

        for i in range(bottom, top - 1, -1):
            res.append(array[i][left])
        left += 1

    return res


def spiralTraverse(array):
    result = []
    if not array:
        return result

    while array:
        # Add first row
        result += array.pop(0)

        # Add every element in last column
        if array and array[0]:
            for row in array:
                result.append(row.pop())

        # Add last row in reverse
        if array:
            result += array.pop()[::-1]

        # Add first column in reverse
        if array and array[0]:
            for row in array[::-1]:
                result.append(row.pop(0))

    return result


if __name__ == '__main__':
    print(spiralTraverse([[1, 2, 3, 4],
                          [12, 13, 14, 5],
                          [11, 16, 15, 6],
                          [10, 9, 8, 7]]))
