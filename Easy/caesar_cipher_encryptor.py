def shift_char(char, shift):
    return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))


def caesarCipherEncryptor(string, key):
    res = ""
    for i in range(len(string)):
        after_shift = shift_char(string[i], key)
        res += after_shift
    return res
