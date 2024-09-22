# Problem : https://www.algoexpert.io/questions/palindrome-check


def isPalindrome(string):
    """
    Checks if a given string is a palindrome.

    Thought Process:
    1. If the string is empty, it is considered a palindrome.
    2. Initialize two pointers, one at the beginning (left) and one at the end (right) of the string.
    3. Compare the characters at both pointers.
    4. If they are not equal, return False.
    5. Move the pointers towards the center and repeat until they meet.
    6. If all characters match, return True.

    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1), as it uses only a constant amount of extra space.
    """
    if not string:
        return True
    left, right = 0, len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True