# Problem : https://www.algoexpert.io/questions/find-three-largest-numbers


def findThreeLargestNumbers(array):
    """
    Finds the three largest numbers in an array.

    Thought Process:
    1. Initialize three variables to store the largest numbers, starting with negative infinity.
    2. Iterate through each number in the array.
    3. Update the largest numbers accordingly:
       - If the current number is larger than the largest, update all three.
       - If it's larger than the second largest but not the largest, update the second and third.
       - If it's larger than the third largest but not the first two, update the third.
    4. Return the three largest numbers in ascending order.

    Time Complexity: O(n), where n is the length of the array.
    Space Complexity: O(1), as no additional space is used beyond a few variables.
    """
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