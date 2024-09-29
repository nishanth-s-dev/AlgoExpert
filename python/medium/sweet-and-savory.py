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