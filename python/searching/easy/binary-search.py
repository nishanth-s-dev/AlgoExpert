# Problem : https://www.algoexpert.io/questions/binary-search

def binarySearch(array, target):
    l, r = 0, len(array) - 1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] < target:
            l = mid + 1
        elif array[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1