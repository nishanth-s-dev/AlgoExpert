# Problem : https://www.algoexpert.io/questions/sweet-and-savory

def sweetAndSavory(dishes, target):
    """
    Finds the pair of sweet and savory dishes that has a total flavor closest
    to a given target without exceeding it.

    Thought process:
    1. Separate the input list `dishes` into two categories: sweet dishes
       (negative values) and savory dishes (positive values).
    2. If either category is empty, return a default result of (0, 0) as no
       valid pairing exists.
    3. Iterate through all combinations of sweet and savory dishes:
       - Calculate the total flavor by summing a sweet dish and a savory dish.
       - If the total flavor does not exceed the target and is closer to the
         target than any previously found combination, update the closest sum
         and store the corresponding sweet and savory dish pair.
    4. Return the pair of dishes that produces the closest total flavor.

    Time: O(m * n) - Where m is the number of sweet dishes and n is the
    number of savory dishes, as each combination is checked.

    Space: O(m + n) - Space is used for storing the lists of sweet and
    savory dishes.
    """
    res = (0, 0)
    closest_flavor = float('inf')

    sweet_dishes = [dish for dish in dishes if dish < 0]
    savory_dishes = [dish for dish in dishes if dish > 0]

    if not sweet_dishes or not savory_dishes:
        return res

    for sweet in sweet_dishes:
        for savory in savory_dishes:
            current_flavor = sweet + savory
            if current_flavor <= target and abs(current_flavor - target) < abs(closest_flavor - target):
                closest_flavor = current_flavor
                res = (sweet, savory)

    return res


def sweetAndSavory(dishes, target):
    """
    Finds the pair of sweet and savory dishes that has a total flavor closest
    to a given target without exceeding it.

    Thought process:
    1. Separate the input list `dishes` into sweet dishes (negative values)
       and savory dishes (positive values). Sort both lists by absolute value
       to process the smallest magnitude dishes first.
    2. If either category is empty, return a default result of (0, 0) since
       no valid pairing exists.
    3. Use a two-pointer approach:
       - Initialize two indices, one for sweet dishes and one for savory dishes.
       - Calculate the total flavor of the current pair. If the total is closer
         to the target than any previously found pair and does not exceed the target,
         update the best pair.
       - Adjust the indices: increment the savory index if the current flavor
         is less than the target, or increment the sweet index if the flavor is greater.
       - If the total matches the target exactly, return the pair immediately.
    4. Continue until one of the lists is exhausted, and return the best pair.

    Time: O(m log m + n log n) - Sorting the sweet and savory dishes takes O(m log m)
    and O(n log n), where m and n are the lengths of the sweet and savory lists, respectively.
    The two-pointer traversal of both lists takes O(m + n).

    Space: O(m + n) - Space is used for storing the lists of sweet and savory dishes.
    """
    best_pair = (0, 0)
    closest_flavor = float('inf')

    sweet_dishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    savory_dishes = sorted([dish for dish in dishes if dish > 0], key=abs)

    if not sweet_dishes or not savory_dishes:
        return best_pair

    sweet_index = 0
    savory_index = 0

    while sweet_index < len(sweet_dishes) and savory_index < len(savory_dishes):
        current_flavor = sweet_dishes[sweet_index] + savory_dishes[savory_index]
        if current_flavor <= target and abs(current_flavor - target) < abs(closest_flavor - target):
            best_pair = (sweet_dishes[sweet_index], savory_dishes[savory_index])
            closest_flavor = current_flavor
        if current_flavor < target:
            savory_index += 1
        elif current_flavor > target:
            sweet_index += 1
        else:
            return best_pair

    return best_pair
