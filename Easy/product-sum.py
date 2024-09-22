# Problem : https://www.algoexpert.io/questions/product-sum

def productSum(array, depth = 1):
    """
    Calculates the product sum of an array, where the sum is multiplied by the depth of nested lists.

    Thought Process:
    1. Initialize a variable to hold the sum.
    2. Iterate through each item in the array.
    3. If the item is a list, recursively call productSum, increasing the depth.
    4. If the item is not a list, add its value to the sum.
    5. After processing all items, return the sum multiplied by the current depth.

    Time Complexity: O(n), where n is the total number of elements in the array, as each element is processed once.
    Space Complexity: O(d), where d is the depth of the nested lists, due to the recursion stack.
    """
    sum = 0
    for item in array:
        if type(item) == list:
            sum += productSum(item, depth + 1)
        else:
            sum += item
    return sum * depth
