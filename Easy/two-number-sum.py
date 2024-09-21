# Problem : https://www.algoexpert.io/questions/two-number-sum

def twoNumberSum(array, target):
    """
    Finds two numbers in the array that add up to the target sum using a brute force approach.

    Thought Process:
    1. Use a nested loop to iterate through each pair of numbers in the array.
    2. For each pair (i, j):
       - Check if the indices are different (i != j).
       - Check if the sum of the two numbers equals the target.
    3. If a matching pair is found, return it as a list.
    4. If no such pair exists after checking all combinations, return an empty list.

    This approach has a time complexity of O(n^2) due to the nested loops and uses O(1) space.
    """
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] + array[j] == target:
                return [array[i], array[j]]
    return []

def twoNumberSum(array, target):
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
    diffMap = {}
    for i in range(len(array)):
        diff = target - array[i]
        if diff in diffMap:
            return [diffMap[diff], i]
        diffMap[array[i]] = i
    pass

print(twoNumberSum([2, 7, 11, 15], 9))