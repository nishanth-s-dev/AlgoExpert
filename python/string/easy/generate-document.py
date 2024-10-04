# Problem : https://www.algoexpert.io/questions/generate-document

from collections import Counter

# O(n * (n + m)) | O(1)
def generateDocument(characters, document):
    """
    Checks if a document can be generated from available characters.

    Thought Process:
    1. For each character in the document, count its occurrences.
    2. Count occurrences of the same character in the available characters.
    3. If the count of any document character exceeds that in the available characters, return False.
    4. If all characters can be matched, return True.
    """
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
    """
    Checks if a document can be generated from available characters using counters.

    Thought Process:
    1. Create a frequency counter for both characters and document.
    2. For each character in the document, check if it exists in the characters counter and if its count is sufficient.
    3. If any character is insufficient, return False.
    4. If all characters are available in sufficient quantity, return True.
    """
    charactersFrequency = Counter(characters)
    documentFrequency = Counter(document)

    for char, count in documentFrequency.items():
        if char not in charactersFrequency or count > charactersFrequency[char]:
            return False

    return True

# O(n + m) | O(k)
def generateDocument(characters, document):
    """
    Checks if a document can be generated from available characters using counters.

    Thought Process:
    1. Create a frequency counter for both characters and document.
    2. For each character in the document, check if it exists in the characters counter and if its count is sufficient.
    3. If any character is insufficient, return False.
    4. If all characters are available in sufficient quantity, return True.
    """
    charactersFrequency = {}
    for char in characters:
        charactersFrequency[char] = charactersFrequency.get(char, 0) + 1

    for char in document:
        if char not in charactersFrequency or charactersFrequency[char] == 0:
            return False
        charactersFrequency[char] = charactersFrequency.get(char) - 1

    return True

print(generateDocument("aheaolabbhb", "helo"))