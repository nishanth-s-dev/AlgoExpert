# Problem : https://www.algoexpert.io/questions/optimal-freelancing

def optimalFreelancing(jobs):
    """
    Calculates the maximum profit from freelancing jobs within given deadlines.

    Thought Process:
    1. Sort jobs by payment in descending order and by deadline in ascending order.
    2. Initialize an array to track available days.
    3. Iterate through each job and try to schedule it on the latest available day before its deadline.
    4. If a day is available, mark it as occupied and add the payment to total profit.
    5. Return the total profit.

    Time Complexity: O(n log n), where n is the number of jobs (due to sorting).
    Space Complexity: O(1), which is constant space for the available days array.
    """
    jobs.sort(key=lambda x: (-x["payment"], x["deadline"]))
    available_days = [False] * 7
    total_profit = 0
    for job in jobs:
        deadline = job['deadline']
        payment = job['payment']

        for day in range(min(7, deadline) - 1, -1, -1):
            if not available_days[day]:
                available_days[day] = True
                total_profit += payment
                break

    return total_profit