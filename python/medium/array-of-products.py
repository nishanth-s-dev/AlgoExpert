# Problem : https://www.algoexpert.io/questions/array-of-products

def arrayOfProducts(array):
    """
    Thought Process:
    The goal is to create a new array where each element at index `i` contains the product of all the numbers in the input array except the one at `i`.

    Approach:
    1. This brute-force approach involves computing the product of every other element in the array except for the current index.
    2. For each element `i` in the array, initialize a `product` variable to 1.
    3. Loop through the array again (inner loop) and multiply the `product` by all elements except for the one at the current index `i`.
    4. Append the result to the `res` array.
    5. Return the `res` array, which will contain the product of all elements except the one at the current index for each position.

    This solution, while simple, has a time complexity of O(n^2), where `n` is the length of the array, since we have nested loops.
    This is inefficient for larger arrays because of the repeated multiplication operations.

    Time Complexity: O(n^2) due to the nested loops.
    Space Complexity: O(n) for storing the result array.
    """

    res = []

    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if j != i:
                product *= array[j]
        res.append(product)

    return res


def arrayOfProducts(array):
    """
    Thought Process:
    The goal is to create a new array where each element at index `i` contains the product of all the numbers in the input array except the one at `i`.

    Approach:
    1. We need to generate a result array `res` where each value at index `i` is the product of all elements in the input array except for the one at index `i`.
    2. Instead of using division to solve this (which would be simpler but less efficient and problematic when zeros are present), we compute the product of elements before and after each index using two arrays:
       - `leftProducts`: Stores the cumulative product of elements to the left of each index (excluding the current index).
       - `rightProducts`: Stores the cumulative product of elements to the right of each index (excluding the current index).
    3. Traverse the array twice:
       - First, populate `leftProducts` by maintaining a running product of elements from the left side.
       - Then, populate `rightProducts` by maintaining a running product of elements from the right side.
    4. Multiply the values in `leftProducts` and `rightProducts` to compute the final product at each index.
    5. Return the `res` array containing the product of all other elements for each index.

    Time Complexity: O(n), where n is the length of the input array, as we make three passes through the array (once to compute left products, once for right products, and once to calculate the result).
    Space Complexity: O(n) for storing the left, right, and result arrays.
    """

    n = len(array)

    res = [1] * n
    leftProducts = [1] * n
    rightProducts = [1] * n

    # Calculate the products to the left of each index
    leftRunningProduct = 1
    for i in range(n):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    # Calculate the products to the right of each index
    rightRunningProduct = 1
    for i in reversed(range(n)):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    # Multiply left and right products for the final result
    for i in range(n):
        res[i] = leftProducts[i] * rightProducts[i]

    return res
