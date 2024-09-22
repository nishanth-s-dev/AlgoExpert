# Problem : https://www.algoexpert.io/questions/caesar-cipher-encryptor

def shift_char(char, shift):
    """
    Shifts a character by a specified number of positions in the alphabet.

    Thought Process:
    1. Convert the character to its zero-based position in the alphabet (0-25).
    2. Add the shift value to this position.
    3. Use modulo 26 to ensure the result wraps around within the alphabet if necessary.
    4. Convert the resulting position back to the corresponding character.

    Time Complexity: O(1), as it involves a constant number of operations.
    Space Complexity: O(1), no additional space is used.
    """
    return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))


def caesarCipherEncryptor(string, key):
    """
    Encrypts a string using the Caesar Cipher technique.

    Thought Process:
    1. Initialize an empty list `res` to store the shifted characters.
    2. Iterate through each character in the input string.
    3. For each character, use the `shift_char` function to get the shifted character.
    4. Append the shifted character to the `res` list.
    5. Use `"".join(res)` to combine all shifted characters into a single string.

    Time Complexity: O(n), where 'n' is the length of the input string,
                     as we process each character exactly once.
    Space Complexity: O(n), as we store the result in a list of the same length.
    """
    res = []
    for i in range(len(string)):
        res.append(shift_char(string[i], key))
    return "".join(res)
