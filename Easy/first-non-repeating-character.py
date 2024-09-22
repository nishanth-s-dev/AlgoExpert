# Problem : https://www.algoexpert.io/questions/first-non-repeating-character


def firstNonRepeatingCharacter(string):
    """
    Finds the index of the first non-repeating character in a string.

    Thought Process:
    1. Iterate through each character in the string.
    2. For each character, check if it appears again in the string.
    3. If it does not appear again, return its index.
    4. If no non-repeating character is found, return -1.

    Time Complexity: O(n^2), where n is the length of the string.
    Space Complexity: O(1), as no additional data structures are used.
    """
    for i in range(len(string)):
        current = string[i]
        for j in range(len(string)):
            if i != j and current == string[j]:
                break
        else:
            return i
    return -1


def firstNonRepeatingCharacter(string):
    """
    Finds the index of the first non-repeating character in a string using a hash map.

    Thought Process:
    1. Create a hash map to count the occurrences of each character in the string.
    2. Iterate through the hash map to find the first character that appears only once.
    3. Return the index of that character from the original string.
    4. If no non-repeating character is found, return -1.

    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1), hashmap won't exceed of length 26, since string only contain lowercase letters.
    """
    hmap = {}
    for s in string:
        hmap[s] = hmap.get(s, 0) + 1

    for key, value in hmap.items():
        if value ==1:
            return string.index(key)
    return -1