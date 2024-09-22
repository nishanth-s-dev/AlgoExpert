# Problem : https://www.algoexpert.io/questions/non-constructible-change

def nonConstructibleChange(coins):
    """
    Determines the minimum amount of change that cannot be created using the given coins.

    Thought Process:
    1. If there are no coins, the smallest non-constructible change is 1.
    2. Sort the list of coins to ensure we can process them in ascending order.
    3. Initialize a variable (`change`) to keep track of the maximum constructible change.
    4. Iterate through each coin:
       - If the current coin is greater than `change + 1`, we cannot construct `change + 1` with the available coins.
         - Return `change + 1` as the minimum non-constructible change.
       - Otherwise, add the coin to the `change` (i.e., increase the maximum constructible change).
    5. If all coins can be used to construct up to `change`, return `change + 1` as the smallest non-constructible change.

    Time Complexity: O(n log n) due to sorting, where n is the number of coins.
    Space Complexity: O(1) additional space, as we are only using a few variables.
    """
    if not coins:
        return 1

    change = 0
    coins.sort()
    for coin in coins:
        if coin > change + 1:
            return change + 1
        else:
            change += coin

    return change + 1