# Problem : https://www.algoexpert.io/questions/reverse-words-in-string

"""
This function reverses the words in a given string while preserving the order of spaces.
It provides two different implementations to achieve this functionality.

Approach 1: Using a Stack
    - Iterate through the characters of the string, building words until a space is encountered.
    - Push each completed word onto a stack.
    - Handle spaces by pushing them onto the stack as well.
    - Finally, pop elements from the stack to construct the reversed string.
    - Time Complexity: O(n), where n is the length of the string.
    - Space Complexity: O(n) for the stack.

Approach 2: Using Lists
    - Use a list to accumulate characters of words and another list for the result.
    - When a space is encountered, join the accumulated characters into a word and append it to the result.
    - After processing the string, reverse the list of words and spaces to construct the final string.
    - Time Complexity: O(n), where n is the length of the string.
    - Space Complexity: O(n) for the result list.
"""

def reverseWordsInString(string):
    stack = []
    temp = ""

    for s in string:
        if s != " ":
            temp += s
        else:
            if temp:
                stack.append(temp)
                temp = ""

            if len(stack) > 0 and stack[-1] == " ":
                stack[-1] += " "
            else:
                stack.append(" ")

    if temp:
        stack.append(temp)

    res = []
    while stack:
        res.append(stack.pop())

    return "".join(res)

def reverseWordsInString(string):
    result = []
    word = []

    for i in range(len(string)):
        if string[i] != " ":
            word.append(string[i])
        else:
            if word:
                result.append(''.join(word))
                word = []
            result.append(" ")

    if word:
        result.append(''.join(word))

    return ''.join(result[::-1])