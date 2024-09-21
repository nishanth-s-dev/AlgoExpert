def minimumWaitingTime(queries):
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
    queries.sort()
    total_waiting_time = 0
    current_waiting_time = 0
    for i in range(len(queries) - 1):
        current_waiting_time = current_waiting_time + queries[i]
        total_waiting_time += current_waiting_time
    return total_waiting_time