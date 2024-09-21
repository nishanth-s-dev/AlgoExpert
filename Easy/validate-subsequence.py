# Problem : https://www.algoexpert.io/questions/validate-subsequence

def isValidSubsequence(array, sequence):
    """
    Finds two numbers in the array that add up to the target sum using a hash map.

    Thought Process:
    1. Initialize an empty dictionary (`diffMap`) to store the numbers we’ve seen so far along with their indices.
    2. Iterate through each number in the array:
       - Calculate the difference (`diff`) needed to reach the target by subtracting the current number from the target.
       - Check if this difference is already in the dictionary:
         - If yes, return the corresponding number and the current index as a list (since they add up to the target).
       - If not, add the current number and its index to the dictionary.
    3. If no such pair exists after checking all numbers, the function implicitly returns `None`.

    This approach has a time complexity of O(n) due to a single pass through the array and O(n) space for the hash map.
    """
    idx = 0
    for item in array:
        if item == sequence[idx]:
            idx += 1
        if idx == len(sequence):
            return True
    return False
