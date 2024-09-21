from collections import Counter

# O(n * (n + m)) | O(1)
def generateDocument(characters, document):
    for documentChar in document:
        counterOne = 0
        counterTwo = 0
        for c in document:
            if c == documentChar:
                counterOne += 1
        for c in characters:
            if c == documentChar:
                counterTwo += 1
        if counterOne > counterTwo:
            return False
    return True


# O(n + m) | O(k + j)
def generateDocument(characters, document):
    charactersFrequency = Counter(characters)
    documentFrequency = Counter(document)

    for char, count in documentFrequency.items():
        if char not in charactersFrequency or count > charactersFrequency[char]:
            return False

    return True

# O(n + m) | O(k)
def generateDocument(characters, document):
    charactersFrequency = {}
    for char in characters:
        charactersFrequency[char] = charactersFrequency.get(char, 0) + 1

    for char in document:
        if char not in charactersFrequency or charactersFrequency[char] == 0:
            return False
        charactersFrequency[char] = charactersFrequency.get(char) - 1

    return True

print(generateDocument("aheaolabbhb", "helo"))