# Problem : https://www.algoexpert.io/questions/selection-sort

def selectionSort(array):
    """
    Sorts an array in ascending order using the Selection Sort algorithm.

    Thought Process:
    1. Iterate through the array, treating each position as the current minimum.
    2. For each position, find the index of the smallest element in the unsorted portion of the array.
    3. Swap the smallest found element with the element at the current position.
    4. Repeat until the entire array is sorted.

    Time Complexity: O(n^2), where n is the length of the array, due to nested loops.
    Space Complexity: O(1), as it sorts the array in place.
    """
    for i in range(len(array)):
        minIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
        array[i], array[minIdx] = array[minIdx], array[i]
    return array