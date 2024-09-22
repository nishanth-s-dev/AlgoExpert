# Problem : https://www.algoexpert.io/questions/run-length-encoding


def runLengthEncoding(s):
    """
    Encodes a string using Run Length Encoding (RLE).

    Thought Process:
    1. Initialize an empty list to hold the encoded segments and a count variable.
    2. Iterate through the string starting from the second character.
    3. If the current character is the same as the previous one and the count is less than 9, increment the count.
    4. If it’s different, append the count and the previous character to the result list, then reset the count.
    5. After the loop, append the last count and character to the result list.
    6. Return the joined result list as a single string.

    Time Complexity: O(n), where n is the length of the input string, as each character is processed once.
    Space Complexity: O(n), as the output can be up to n characters in length in the worst case.
    """
    res = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1] and count < 9:
            count += 1
        else:
            res.append(str(count) + s[i - 1])
            count = 1

    res.append(str(count) + s[-1])
    return "".join(res)