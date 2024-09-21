# Problem : https://www.algoexpert.io/questions/sorted-squared-array

def sortedSquaredArray(array):
    """
    Squares each element and sorts the resulting array.

    Thought Process:
    1. Use a list comprehension to create a new list with the squares of each element.
    2. Sort the squared list.
    3. This solution leverages Python's built-in `sorted` function.

    Time Complexity: O(n log n) because sorting takes O(n log n) time.
    Space Complexity: O(1) extra space if we ignore the space used to hold the result.
    """
    return sorted([num ** 2 for num in array])


### IMPORTANT: Too confusing - Not recommended
def sortedSquaredArray(array):
    """
    Merges squares of negative and positive parts of the array.

    Thought Process:
    1. Split the array into negative and non-negative parts.
    2. Use two pointers to merge squares of these two parts:
       - Compare the absolute values of elements pointed to by both pointers.
       - Append the smaller squared value to the result list.
    3. Append remaining elements from either part, if any.

    Time Complexity: O(n) for a single pass through the array.
    Space Complexity: O(n) for the resulting list.
    """
    res = []
    if array[0] >= 0:
        for num in array:
            res.append(num ** 2)
        return res

    negative_index = -1
    positive_index = len(array)
    for i in range(len(array)):
        if array[i] >= 0:
            negative_index = i - 1
            positive_index = i
            break
    else:
        negative_index = len(array) - 1

    while negative_index >= 0 and positive_index < len(array):
        negative_value = abs(array[negative_index])
        positive_value = abs(array[positive_index])
        if negative_value > positive_value:
            res.append(positive_value ** 2)
            positive_index += 1
        elif positive_value > negative_value:
            res.append(negative_value ** 2)
            negative_index -= 1
        else:
            res.append(negative_value ** 2)
            res.append(positive_value ** 2)
            positive_index += 1
            negative_index -= 1

    for i in range(negative_index, -1, -1):
        res.append(array[i] ** 2)

    for i in range(positive_index, len(array)):
        res.append(array[i] ** 2)

    return res


def sortedSquaredArray(array):
    """
    Uses two pointers to create a sorted array of squares.

    Thought Process:
    1. Initialize two pointers at the start and end of the array.
    2. Compare absolute values of elements at these pointers.
    3. Place the square of the larger absolute value at the end of the result list.
    4. Move the corresponding pointer inward and repeat until all elements are processed.

    Time Complexity: O(n) since each element is processed once.
    Space Complexity: O(n) for the resulting list.
    """
    res = [0 for _ in array]

    start, end = 0, len(array) - 1

    for idx in reversed(range(len(array))):
        start_val = abs(array[start])
        end_val = abs(array[end])
        if start_val < end_val:
            res[idx] = end_val ** 2
            end -= 1
        else:
            res[idx] = start_val ** 2
            start += 1
    return res
