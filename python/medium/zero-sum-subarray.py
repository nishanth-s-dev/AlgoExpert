# Problem : https://www.algoexpert.io/questions/zero-sum-subarray

def arrayOfProducts(array):
    """
    Thought Process:
    The goal is to create a new array where each element at index `i` contains the product of all the numbers in the input array except the one at `i`.

    Approach:
    1. This brute-force approach involves computing the product of every other element in the array except for the current index.
    2. For each element `i` in the array, initialize a `product` variable to 1.
    3. Loop through the array again (inner loop) and multiply the `product` by all elements except for the one at the current index `i`.
    4. Append the result to the `res` array.
    5. Return the `res` array, which will contain the product of all elements except the one at the current index for each position.

    This solution, while simple, has a time complexity of O(n^2), where `n` is the length of the array, since we have nested loops.
    This is inefficient for larger arrays because of the repeated multiplication operations.

    Time Complexity: O(n^2) due to the nested loops.
    Space Complexity: O(n) for storing the result array.
    """

    res = []

    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if j != i:
                product *= array[j]
        res.append(product)

    return res


def zeroSumSubarray(nums):
    """
    Thought Process:
    The goal is to determine whether there exists a contiguous subarray within the given array `nums` that sums to zero.

    Approach:
    1. If the input array is empty, return False, as there can be no subarray.
    2. If the total sum of the array is zero, return True immediately, as the entire array itself is a valid subarray.
    3. Calculate the prefix sum for the array:
       - The prefix sum at index `i` represents the sum of all elements from the start of the array up to index `i`.
       - Store these prefix sums in a list called `prefixSum`.
    4. After calculating the prefix sums, check for duplicates:
       - If any prefix sum occurs more than once, it implies that the sum of the elements between the two occurrences of the same prefix sum is zero (due to the properties of cumulative sums).
    5. Return True if there are duplicates in the `prefixSum`, indicating the presence of a zero-sum subarray; otherwise, return False.

    Time Complexity: O(n), where n is the length of the array, since we compute the prefix sums in one pass and check for duplicates using a set.
    Space Complexity: O(n) for storing the prefix sums.

    Note: This approach assumes that the input array can contain both positive and negative integers, including zero.
    """

    if not nums:
        return False

    if sum(nums) == 0:
        return True

    prefixSum = [0] * len(nums)
    prefixSum[0] = nums[0]
    for i in range(1, len(nums)):
        prefixSum[i] = nums[i] + prefixSum[i - 1]

    return len(prefixSum) != len(set(prefixSum))
