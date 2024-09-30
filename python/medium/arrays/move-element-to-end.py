# Problem : https://www.algoexpert.io/questions/move-element-to-end

def moveElementToEnd(array, toMove):
    """
    This function moves all instances of a specified element (`toMove`) in the input array to the end of the array.
    The relative order of the other elements is preserved. It modifies the array in-place and returns the modified array.

    Approach:
    1. Use two pointers, `left` and `right`, starting at the beginning and end of the array respectively.
    2. Move the `right` pointer towards the left until it points to an element that is not `toMove`.
    3. If the `left` pointer points to an element that is `toMove`, swap it with the element at the `right` pointer.
    4. Move the `left` pointer to the right after each check to continue processing.
    5. Repeat until the `left` pointer meets the `right` pointer.

    Time Complexity: O(n), where `n` is the length of the array, as each element is processed at most once.
    Space Complexity: O(1), as the function operates in-place without using additional memory.

    Args:
    - array: List of integers where elements are to be rearranged.
    - toMove: The integer element that needs to be moved to the end of the array.

    Returns:
    - array: The modified list with all instances of `toMove` moved to the end.
    """
    left, right = 0, len(array) - 1

    while left < right:
        while right > left and array[right] == toMove:
            right -= 1
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1

    return array
