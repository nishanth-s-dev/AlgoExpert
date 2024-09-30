# Problem : https://www.algoexpert.io/questions/three-number-sum

def threeNumberSum(array, targetSum):
    """
    This function finds all unique triplets in a given array that sum up to a specified target value.
    It leverages the two-pointer technique after sorting the array to efficiently find these triplets.

    Approach:
    1. Sort the input array to apply the two-pointer approach.
    2. Iterate through the array with an index `i`, and for each element at `i`, use two pointers:
        - `left` starts right after `i`.
        - `right` starts at the end of the array.
    3. Calculate the current sum of the triplet formed by `array[i]`, `array[left]`, and `array[right]`.
    4. If the sum matches the target, add the triplet to the result list and move both pointers inward.
    5. If the sum is less than the target, move the `left` pointer to the right to increase the sum.
    6. If the sum is greater than the target, move the `right` pointer to the left to decrease the sum.

    Time Complexity: O(n^2), where `n` is the length of the array, due to the nested loops and two-pointer technique.
    Space Complexity: O(m), where `m` is the number of unique triplets in the result list.

    Args:
    - array: List of integers.
    - targetSum: The desired sum of triplets.

    Returns:
    - res: A list of lists containing unique triplets that sum up to `targetSum`.
    """
    array.sort()
    res = []
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                res.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return res


# This solution is useful for array containing duplicate values
def threeNumberSum(array, targetSum):
    """
    This function finds all unique triplets in a given array that sum up to a specified target value.
    The array may contain duplicate values, but the function ensures that each triplet is unique in the result set.

    Approach:
    1. Sort the input array to handle duplicates and to use the two-pointer technique effectively.
    2. Iterate through the array with an index `i`, and for each element at `i`, use two pointers, `j` (left) and `k` (right).
    3. Calculate the current sum of the triplet formed by `array[i]`, `array[j]`, and `array[k]`.
    4. If the sum matches the target, add the triplet to the result list and move both pointers inward.
    5. If the sum is less than the target, move the left pointer (`j`) to the right.
    6. If the sum is greater than the target, move the right pointer (`k`) to the left.
    7. Skip duplicate elements to ensure unique triplets in the result list.

    Time Complexity: O(n^2), where `n` is the length of the array, due to the nested loops and two-pointer technique.
    Space Complexity: O(m), where `m` is the number of unique triplets in the result list.

    Args:
    - array: List of integers that may contain duplicates.
    - targetSum: The desired sum of triplets.

    Returns:
    - res: A list of lists containing unique triplets that sum up to `targetSum`.
    """
    array.sort()
    res = []
    for i in range(len(array)):
        j = i + 1
        k = len(array) - 1
        while j < k:
            currentSum = array[i] + array[j] + array[k]
            if currentSum == targetSum:
                res.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            if currentSum < targetSum:
                j += 1
                while j < len(array) - 1 and array[j] == array[j + 1]:
                    j += 1
            if currentSum > targetSum:
                k -= 1
                while k >= 0 and array[k] == array[k - 1]:
                    k -= 1

    return res