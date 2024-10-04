# Problem : https://www.algoexpert.io/questions/median-of-two-sorted-arrays

# TODO : Need to add more optimal solution

# o((n + m)log(n + m)) | O(n + m)
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    array = arrayOne + arrayTwo
    array.sort()

    length = len(array)
    if length % 2 != 0:
        mid = length // 2
        return array[mid]

    mid = length // 2
    return (array[mid] + array[mid - 1]) / 2