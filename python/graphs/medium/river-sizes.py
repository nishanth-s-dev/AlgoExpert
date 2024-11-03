# https://www.algoexpert.io/questions/river-sizes

def riverSizes(matrix):
    visitedNodes = set()
    result = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (row, col) in visitedNodes:
                continue
            traverseNode(row, col, matrix, visitedNodes, result)

    return result

def traverseNode(row, col, matrix, visitedNodes, result):
    currentRiverSize = 0
    nodeToExplore = [(row, col)]
    while nodeToExplore:
        currentNode = nodeToExplore.pop()
        currentRow, currentCol = currentNode

        if currentNode in visitedNodes:
            continue
        visitedNodes.add(currentNode)

        if matrix[currentRow][currentCol] == 0:
            continue
        currentRiverSize += 1

        unvisitedNeighbors = getUnvisitedNeighbors(currentNode, matrix, visitedNodes)
        for neighbor in unvisitedNeighbors:
            nodeToExplore.append(neighbor)

    if currentRiverSize != 0:
        result.append(currentRiverSize)

def getUnvisitedNeighbors(node, matrix, visitedNodes):
    row, col = node

    unvisitedNeighbors = []

    up = (row - 1, col)
    right = (row, col + 1)
    down = (row + 1, col)
    left = (row, col - 1)

    if up not in visitedNodes and row > 0:
        unvisitedNeighbors.append(up)
    if right not in visitedNodes and col < len(matrix[0]) - 1:
        unvisitedNeighbors.append(right)
    if down not in visitedNodes and row < len(matrix) - 1:
        unvisitedNeighbors.append(down)
    if left not in visitedNodes and col > 0:
        unvisitedNeighbors.append(left)

    return unvisitedNeighbors


if __name__ == '__main__':
    array = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    print(riverSizes(array))