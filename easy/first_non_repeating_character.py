# O(n) | o(1)
# Constant space is because, only lowercase letters in string, not anything. So it will never exceed len 26

def firstNonRepeatingCharacter(string):
    hmap = {}
    for s in string:
        hmap[s] = hmap.get(s, 0) + 1

    for key, value in hmap.items():
        if value ==1:
            return string.index(key)
    return -1


def firstNonRepeatingCharacter(string):
    for i in range(len(string)):
        current = string[i]
        for j in range(len(string)):
            if i != j and current == string[j]:
                break
        else:
            return i
    return -1
