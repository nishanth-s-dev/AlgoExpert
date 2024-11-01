# https://www.algoexpert.io/questions/kadane's-algorithm

# O(n^2) Time
def kadanesAlgorithm(array):
    maxSum = float('-inf')
    for i in range(len(array)):
        for j in range(i, len(array)):
            currentSum = sum(array[i : j + 1])
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum


if __name__ == '__main__':
    print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))