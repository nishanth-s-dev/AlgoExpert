# Problem : https://www.algoexpert.io/questions/missingNumbers
from unittest.mock import right


def missingNumbers(nums):
    """
    Finds the two missing numbers from a sequence containing 'n-2' elements
    from the range [1, n], where n is the length of the sequence plus 2.

    Thought process:
    1. We are given a list of numbers where exactly two numbers are missing
       from the full range [1, n], where n is the length of the original list
       plus 2.
    2. Convert the list to a set for efficient lookup, as checking membership
       in a set is O(1).
    3. Iterate over the range [1, n] and for each number, check if it is in
       the set. If it is not, add it to the result list.
    4. Return the result list containing the two missing numbers.

    Time : O(n)
    Space : O(n)
    """

    n = len(nums) + 2
    nums_set = set(nums)
    res = []
    for i in range(1, n + 1):
        if i not in nums_set:
            res.append(i)

    return res

def missingNumbers(nums):
    """
    Finds the two missing numbers from a sequence containing 'n-2' elements
    from the range [1, n], where n is the length of the sequence plus 2.

    Thought process:
    1. Calculate the expected total sum of numbers from 1 to n using the
       formula n * (n + 1) // 2.
    2. Calculate the actual sum of the numbers present in the input list.
    3. The difference between the expected total sum and the actual sum gives
       us the sum of the two missing numbers.
    4. Divide the missing sum by 2 to find the average of the two missing
       numbers. This allows us to partition the range into two parts.
    5. Calculate the total sum of the numbers from 1 to the average of the
       missing numbers and also the total sum from the average + 1 to n.
    6. Iterate through the input list and accumulate sums for numbers less
       than or equal to the average and those greater than the average.
    7. The missing numbers can be found by subtracting the actual sums from
       the total sums calculated earlier.

    Time Complexity: O(n) - We iterate through the list once to calculate
    the sums.
    Space Complexity: O(1) - We use a constant amount of extra space.
    """
    n = len(nums) + 2

    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_sum = total_sum - actual_sum
    missing_sum_avg = missing_sum // 2

    actual_left_sum = 0
    actual_right_sum = 0

    total_left_sum = missing_sum_avg * (missing_sum_avg + 1) // 2
    total_right_sum = n * (n + 1) // 2 - total_left_sum                 # n = len(nums) + 2

    # Real Formula
    # total_right_sum = (len(nums) + 2) * (len(nums) + 3) // 2 - (missing_sum_avg * (missing_sum_avg + 1) // 2)

    # Simple way, But will take n time
    # total_left_sum = sum(range(1, missing_sum_avg + 1))
    # total_right_sum = sum(range(missing_sum_avg + 1, len(nums) + 3))

    for num in nums:
        if num <= missing_sum_avg:
            actual_left_sum += num
        else:
            actual_right_sum += num


    return [total_left_sum - actual_left_sum, total_right_sum - actual_right_sum]


if __name__ == '__main__':
    print(missingNumbers([1, 2, 5]))