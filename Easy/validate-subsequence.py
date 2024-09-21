# Problem : https://www.algoexpert.io/questions/validate-subsequence

def isValidSubsequence(array, sequence):
    """
    Checks if the given sequence is a valid subsequence of the array.

    Thought Process:
    1. Initialize an index (`idx`) to track the position in the sequence.
    2. Iterate through each item in the array:
       - If the current item matches the current element in the sequence (at index `idx`):
         - Increment the index to check the next element in the sequence.
       - If `idx` reaches the length of the sequence, it means all elements have been found in order, so return True.
    3. If the loop completes without finding all elements of the sequence, return False.

    This approach has a time complexity of O(n), where n is the length of the array, and O(1) space complexity since no additional data structures are used.
    """
    idx = 0
    for item in array:
        if item == sequence[idx]:
            idx += 1
        if idx == len(sequence):
            return True
    return False
