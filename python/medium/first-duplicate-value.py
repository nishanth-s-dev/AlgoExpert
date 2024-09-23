# Problem : https://www.algoexpert.io/questions/first-duplicate-value

"""
This function returns the first duplicate value it encounters in the input array.
It provides three different implementations for solving the problem, each with varying time and space complexities.

Approach 1: Brute Force (Nested Loops)
    - Use two nested loops to compare each element with every other element that comes after it.
    - Track the minimum index of any duplicate found.
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)

Approach 2: Using a HashSet
    - Traverse the array and keep track of elements seen so far using a hash set.
    - If an element is encountered again, it is returned as the first duplicate.
    - Time Complexity: O(n)
    - Space Complexity: O(n)

Approach 3: In-Place Modification
    - Traverse the array and use the absolute value of each element as an index.
    - If the value at that index is negative, it means the current element is a duplicate.
    - Otherwise, mark the value at that index as negative.
    - This modifies the original array, but works with O(1) space.
    - Time Complexity: O(n)
    - Space Complexity: O(1)
"""

def firstDuplicateValue(array):
    minIndex = len(array)

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                minIndex = min(minIndex, j)

    return array[minIndex] if minIndex != len(array) else -1

def firstDuplicateValue(array):
    hashset = set()
    for num in array:
        if num in hashset:
            return num
        else:
            hashset.add(num)
    return -1

"""
Key NOTE :
 * Array allowed to mutate
 * Array only contains value from 1 - n. Where n in length of the array. 
 * Ex: [1, 2, 2, 4, 5], It should not contain value greater than len(array). Ex: [1, 2, 2, 4, 7]
"""
def firstDuplicateValue(array):
    for i in range(len(array)):
        index = abs(array[i]) - 1
        if array[index] < 0:
            return abs(array[i])
        else:
            array[index] = array[index] * -1
    return -1