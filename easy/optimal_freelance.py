def optimalFreelancing(jobs):
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