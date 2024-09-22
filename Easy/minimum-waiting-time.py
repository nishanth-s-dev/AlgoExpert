# Problem : https://www.algoexpert.io/questions/minimum-waiting-time

def minimumWaitingTime(queries):
    """
    Calculates the minimum total waiting time for a list of queries using a prefix sum.

    Thought Process:
    1. Sort the queries in ascending order.
    2. Calculate the prefix sum of the sorted queries.
    3. Sum the prefix sums, excluding the last element, to get the total waiting time.
    4. Return the total waiting time.

    Time Complexity: O(n log n), where n is the number of queries (due to sorting).
    Space Complexity: O(n), for the prefix sum array.
    """
    queries.sort()
    prefix_sum = prefix(queries)
    res = 0
    for i in range(len(prefix_sum) - 1):
        res += prefix_sum[i]
    return res

def prefix(queries):
    res = [0] * len(queries)
    res[0] = queries[0]
    for i in range(1, len(queries)):
        res[i] = res[i-1] + queries[i]
    return res

# without prefix sum array
def minimumWaitingTimeWithoutPrefixSumArray(queries):
    """
    Calculates the minimum total waiting time for a list of queries without using a prefix sum array.

    Thought Process:
    1. Sort the queries in ascending order.
    2. Initialize total waiting time and current waiting time.
    3. Iterate through the sorted queries, updating current waiting time and accumulating total waiting time.
    4. Return the total waiting time.

    Time Complexity: O(n log n), where n is the number of queries (due to sorting).
    Space Complexity: O(1), as it uses a constant amount of extra space.
    """
    queries.sort()
    total_waiting_time = 0
    current_waiting_time = 0
    for i in range(len(queries) - 1):
        current_waiting_time = current_waiting_time + queries[i]
        total_waiting_time += current_waiting_time
    return total_waiting_time