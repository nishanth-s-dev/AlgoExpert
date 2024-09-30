# Problem : https://www.algoexpert.io/questions/longest-peak

def longestPeak(array):
    """
    Finds the length of the longest peak in a list of integers. A peak is defined
    as an element that is greater than its immediate neighbors.

    Thought process:
    1. Iterate through the array starting from the second element to the second
       last element, checking if the current element is a peak (greater than
       its neighbors).
    2. When a peak is found, initialize pointers to expand left and right to
       count the total number of contiguous elements forming the peak.
    3. Continue expanding left while the elements are increasing and expand
       right while the elements are decreasing to determine the full length
       of the peak.
    4. Keep track of the maximum length of any peak found during the iterations
       and return it.

    Time: O(n) - The algorithm makes a single pass through the array while
    expanding for each peak found.
    Space: O(1) - Only a constant amount of space is used for variables.
    """
    res = 0

    if len(array) < 3:
        return res

    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] > array[i + 1]:
            left, right, temp = i - 1, i + 1, 3

            while left > 0 and array[left] > array[left - 1]:
                temp += 1
                left -= 1

            while right < len(array) - 1 and array[right] > array[right + 1]:
                temp += 1
                right += 1

            res = max(temp, res)

    return res

if __name__ == '__main__':
    print(longestPeak([1, 2, 3, 4, 5, 1]))
