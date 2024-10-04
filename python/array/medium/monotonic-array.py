# Problem : https://www.algoexpert.io/questions/monotonic-array


def isMonotonic(array):
    """
    Thought Process:
    The goal is to check whether the array is monotonic, meaning it must be entirely non-increasing or non-decreasing.

    Approach:
    1. Handle edge cases: If the array is empty or contains a single element, it is trivially monotonic, so return True.
    2. Find the first pair of adjacent elements that are not equal to determine the trend (increasing or decreasing).
    3. If all elements are equal, the array is monotonic, so return True.
    4. Based on the trend, use a flag (`isIncreasing`) to track whether the array is increasing or decreasing.
    5. Traverse the array, checking whether all elements follow the identified trend:
       - If `isIncreasing` is True, ensure no element is smaller than the previous one.
       - If `isIncreasing` is False, ensure no element is larger than the previous one.
    6. If any element violates the trend, return False.
    7. If no violations occur, return True.

    Time Complexity: O(n), where n is the length of the array, since we traverse the array once.
    """
    if not array or len(array) == 1:
        return True

    idx = 1
    while idx < len(array) and array[idx] == array[idx - 1]:
        idx += 1

    if idx == len(array):
        return True
    else:
        isIncreasing = True if array[idx - 1] < array[idx] else False

    for i in range(1, len(array)):
        if (isIncreasing and array[i - 1] > array[i]) or (not isIncreasing and array[i - 1] < array[i]):
            return False

    return True

def isMonotonic(array):
    """
    Thought Process:
    The goal is to check whether the array is monotonic, meaning it is either non-increasing or non-decreasing.

    Approach:
    1. If the array has 2 or fewer elements, it is trivially monotonic, so return True.
    2. Initialize two flags: `isIncreasing` and `isDecreasing`. Both are set to True initially.
       - `isIncreasing` will track if the array is non-decreasing (elements are increasing or remain constant).
       - `isDecreasing` will track if the array is non-increasing (elements are decreasing or remain constant).
    3. Traverse the array starting from the second element:
       - If an element is greater than the previous one, set `isDecreasing` to False (the array cannot be non-increasing).
       - If an element is smaller than the previous one, set `isIncreasing` to False (the array cannot be non-decreasing).
    4. After the loop, if either `isIncreasing` or `isDecreasing` is still True, the array is monotonic, so return True.
    5. If both flags are False, the array is neither non-increasing nor non-decreasing, so return False.

    Time Complexity: O(n), where n is the length of the array, since we traverse the array once.
    """

    if len(array) <= 2:
        return True

    isDecreasing = True
    isIncreasing = True

    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            isDecreasing = False
        if array[i - 1] > array[i]:
            isIncreasing = False

    return isIncreasing or isDecreasing