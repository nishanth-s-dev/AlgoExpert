# https://www.algoexpert.io/questions/group-anagrams


# O(n * k (log k)) | O(n)
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    return list(anagrams.values())

# O(n * k) | O(n)
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        frequency_array = [0] * 26
        for c in word:
            current_index = int(ord(c) - ord('a'))
            frequency_array[current_index] += 1
        immutable_frequency_array = tuple(frequency_array)
        if immutable_frequency_array not in anagrams:
            anagrams[immutable_frequency_array] = [word]
        else:
            anagrams[immutable_frequency_array].append(word)
    return list(anagrams.values())
