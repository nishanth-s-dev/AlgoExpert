# Problem : https://www.algoexpert.io/questions/four-number-sum
# TODO : Need to add optimal solution

def fourNumberSum(array, targetSum):
    """
    Finds all unique combinations of four numbers from the input array that
    sum up to a specified target sum.

    Thought process:
    1. Use a set called `seen` to keep track of unique combinations of four
       numbers to avoid duplicates in the results.
    2. Use four nested loops to iterate through all possible combinations of
       indices (i, j, k, l) in the array.
    3. For each combination, ensure that the indices are distinct by checking
       that the set of indices has a length of 4.
    4. Calculate the current sum of the four selected numbers and compare it
       to the target sum:
       - If the sum matches the target, create a sorted tuple of the combination
         and check if it has been seen before. If not, add it to the set and
         append the corresponding list to the results.
    5. Return the list of unique combinations that add up to the target sum.

    Time: O(n^4) - The algorithm has four nested loops, leading to a time complexity
    that scales with the fourth power of the length of the array.

    Space: O(k) - Where k is the number of unique combinations found. The space
    is used for the results and the `seen` set.
    """
    seen = set()
    res = []
    for i in range(len(array)):
        for j in range(i, len(array)):
            for k in range(j, len(array)):
                for l in range(k, len(array)):
                    if len({i, j, k, l}) == 4:
                        current_target = array[i] + array[j] + array[k] + array[l]
                        if current_target == targetSum:
                            combination = tuple(sorted([array[i], array[j], array[k], array[l]]))
                            if combination not in seen:
                                seen.add(combination)
                                res.append([array[i], array[j], array[k], array[l]])
    return res