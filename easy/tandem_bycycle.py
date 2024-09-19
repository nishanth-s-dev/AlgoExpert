def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    res = 0
    if fastest:
        redPointer = 0
        bluePointer = len(blueShirtSpeeds) - 1
        while redPointer < len(redShirtSpeeds) and bluePointer >= 0:
            res += max(redShirtSpeeds[redPointer], blueShirtSpeeds[bluePointer])
            redPointer += 1
            bluePointer -= 1
    else:
        for i in range(len(redShirtSpeeds)):
            res += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return res

"""
[5, 5, 3, 9, 2]
[3, 6, 7, 2, 1]

[2, 3, 5, 5, 9]
[1, 2, 3, 6, 7]

min = [(2, 1), (3, 2), (5, 3), (5, 6), (9, 7)] == [2, 3, 5, 6, 9] = 25
max = [(2, 7), (3, 6), (5, 3), (5, 2), (9, 1)] == [7, 6, 5, 5, 9] = 32
"""