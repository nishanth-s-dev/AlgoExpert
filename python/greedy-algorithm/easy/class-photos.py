# Problem : https://www.algoexpert.io/questions/class-photos


def classPhotos(redShirtHeights, blueShirtHeights):
    """
    Determines if a class photo can be taken with two rows of students,
    where one row is consistently taller than the other.

    Thought Process:
    1. Sort both `redShirtHeights` and `blueShirtHeights` arrays in ascending order.
    2. Determine which group should be in the back row based on the first elements
       (the shortest students in each group). The group with the taller shortest
       student will be the back row.
    3. Iterate through the heights of both groups and check:
       - If `firstGreater` is 'blue', each student in `blueShirtHeights` must be taller than the corresponding student in `redShirtHeights`.
       - If `firstGreater` is 'red', each student in `redShirtHeights` must be taller than the corresponding student in `blueShirtHeights`.
    4. If any student in the back row is not taller than the corresponding student in the front row, return `False`.
    5. If all conditions are met, return `True`.

    Time Complexity: O(n log n), where 'n' is the number of students in each group.
                     This is due to the sorting step, as comparison of heights is O(n).
    Space Complexity: O(1), as no additional space is used other than the input lists.
    """
    redShirtHeights.sort()
    blueShirtHeights.sort()

    firstGreater = 'red' if redShirtHeights[0] > blueShirtHeights[0] else 'blue'
    print(firstGreater)
    for i in range(len(redShirtHeights)):
        if firstGreater == 'blue' and blueShirtHeights[i] <= redShirtHeights[i]:
            return False
        if firstGreater == 'red' and redShirtHeights[i] <= blueShirtHeights[i]:
            return False

    return True