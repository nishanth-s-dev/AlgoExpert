# Problem : https://www.algoexpert.io/questions/insertion-sort

def insertionSort(array):
    """
    Sorts an array in ascending order using the Insertion Sort algorithm.

    Thought Process:
    1. Iterate through each element in the array starting from the second element.
    2. For each element, store its value and compare it with the elements before it.
    3. Shift elements that are greater than the current element to the right.
    4. Insert the current element into its correct position.
    5. Continue until the entire array is sorted.

    Time Complexity: O(n^2), where n is the length of the array, due to nested loops.
    Space Complexity: O(1), as it sorts the array in place.
    """
    for i in range(len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and current < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array