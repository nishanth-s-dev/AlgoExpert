from collections import defaultdict


def semordnilap(words):
    hs = set()
    semordnilaps = []

    for word in words:
        reversed_word = word[::-1]
        if reversed_word in hs:
            semordnilaps.append((word, reversed_word))
        hs.add(word)

    return semordnilaps