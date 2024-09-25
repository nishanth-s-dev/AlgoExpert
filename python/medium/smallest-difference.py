# Problem : https://www.algoexpert.io/questions/smallest-difference


def smallestDifference(arrayOne, arrayTwo):
    """
    Thought Process:
    The goal is to find the pair of numbers (one from each array) whose difference is the smallest.

    Approach:
    1. Sort both arrays in ascending order. Sorting helps in utilizing two-pointer technique, as the arrays will be in order.
    2. Initialize two pointers (`pointerOne` for `arrayOne` and `pointerTwo` for `arrayTwo`) and a variable `diff` to keep track of the smallest difference.
    3. Traverse both arrays using the two pointers. Compare the numbers at the current pointer positions in both arrays.
    4. If the number in `arrayOne` is smaller, increment `pointerOne`. If the number in `arrayTwo` is smaller, increment `pointerTwo`. This helps reduce the difference between the numbers.
    5. If the numbers are equal, return the pair immediately, since the difference is zero (the smallest possible).
    6. Update the result if the current difference is smaller than the previously tracked `diff`.
    7. The loop continues until one of the arrays is exhausted, and the smallest difference pair is returned.

    Time Complexity: O(nlog(n) + mlog(m)), where n and m are the lengths of the two arrays due to sorting. The while loop runs in O(n + m) time.
    """
    arrayOne.sort()
    arrayTwo.sort()

    pointerOne = pointerTwo = 0
    diff = float("inf")
    res = []

    while pointerOne < len(arrayOne) and pointerTwo < len(arrayTwo):
        currentDiff = abs(arrayOne[pointerOne] - arrayTwo[pointerTwo])
        firstNum = arrayOne[pointerOne]
        secondNum = arrayTwo[pointerTwo]

        if currentDiff < diff:
            res = [firstNum, secondNum]
            diff = currentDiff

        if firstNum < secondNum:
            pointerOne += 1
        elif firstNum > secondNum:
            pointerTwo += 1
        else:
            return [firstNum, secondNum]

    return res