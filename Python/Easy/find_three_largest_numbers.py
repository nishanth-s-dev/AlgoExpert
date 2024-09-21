def findThreeLargestNumbers(array):
    max1 = max2 = max3 = float('-inf')
    for number in array:
        if number > max1:
            max3 = max2
            max2 = max1
            max1 = number
        elif number > max2:
            max3 = max2
            max2 = number
        elif number > max3:
            max3 = number
    return [max3, max2, max1]