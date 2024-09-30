# Problem : https://www.algoexpert.io/questions/merge-overlapping-intervals


def mergeOverlappingIntervals(intervals):
    """
    Merges overlapping intervals in a list of intervals.

    Thought process:
    1. Sort the intervals based on the starting point of each interval to ensure
       they are processed in the correct order.
    2. Initialize the `merged_intervals` list with the first interval.
    3. Iterate through the remaining intervals, and for each interval:
       - If it overlaps with the last interval in the `merged_intervals` list
         (i.e., the current interval's start is less than or equal to the last
         interval's end), merge them by updating the end of the last interval.
       - If it doesn't overlap, append the current interval to the `merged_intervals` list.
    4. Return the `merged_intervals` list, which contains all merged intervals.

    Time: O(n log n) - Sorting the intervals takes O(n log n), and iterating
    through them takes O(n).
    Space: O(n) - The space used is proportional to the input size.
    """
    intervals.sort(key = lambda interval : interval[0])
    merged_intervals = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = merged_intervals[-1][1]

        if start <= lastEnd:
            merged_intervals[-1][1] = max(end, lastEnd)
        else:
            merged_intervals.append([start, end])
    return merged_intervals



if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    mergedIntervals = mergeOverlappingIntervals(intervals)
    print(mergedIntervals)