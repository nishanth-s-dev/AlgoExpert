# Problem : https://www.algoexpert.io/questions/majority-element

def majorityElement(nums):
    """
    Finds the majority element in a list of integers, where the majority element
    is defined as the element that appears more than n/2 times (n is the size of the list).

    The algorithm uses the Boyer-Moore Voting Algorithm which works in two phases:
    1. **Candidate Selection**: It iterates through the list to find a potential
       candidate for the majority element by maintaining a count. If the count
       reaches zero, the current number becomes the candidate, and the count is reset.
       If the current number matches the candidate, the count is incremented;
       otherwise, it is decremented.

    2. **Candidate Verification**: After determining the candidate, the algorithm
       makes a second pass through the list to count its occurrences and verify
       if it indeed appears more than n/2 times.

    Returns:
        - The majority element if found, otherwise -1.

    Time Complexity: O(n) - The algorithm makes two passes over the list of size n.

    Space Complexity: O(1) - Only a constant amount of space is used for
    the candidate and count variables.
    """
    candidate, count = None, 0

    for num in nums:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    res = candidate if count > len(nums) // 2 else -1
    return res

if __name__ == '__main__':
    print(majorityElement([4, 5, 5]))