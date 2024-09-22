# Problem : https://www.algoexpert.io/questions/bubble-sort

def bubbleSort(array):
    """
    Sorts an array in ascending order using the Bubble Sort algorithm.

    Thought Process:
    1. Iterate through the array multiple times.
    2. During each pass, compare adjacent elements.
    3. If an element is greater than the one following it, swap them.
    4. This process moves the largest unsorted element to its correct position at the end of the array in each pass.
    5. Repeat until the array is sorted.

    Time Complexity:
    - Worst and Average Case: O(n^2), due to nested loops.
    - Best Case: O(n), when the array is already sorted.

    Space Complexity: O(1), as it sorts the array in place.
    """
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array