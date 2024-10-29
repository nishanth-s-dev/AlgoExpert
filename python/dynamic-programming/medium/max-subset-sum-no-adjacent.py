# https://www.algoexpert.io/questions/max-subset-sum-no-adjacent

def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    return max(array[0] + maxSubsetSumNoAdjacent(array[2:]), maxSubsetSumNoAdjacent(array[1:]))

def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    res = []
    res.append(array[0])
    res.append(max(array[0], array[1]))
    for i in range(2, len(array)):
        res.append(max(res[i - 2] + array[i], res[i - 1]))
    return res[-1]

def main():
    array = [75, 105, 120, 75, 90, 135]
    print(maxSubsetSumNoAdjacent(array))

if __name__ == '__main__':
    main()

