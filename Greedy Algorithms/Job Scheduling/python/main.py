def job_scheduling(jobs):
    # jobs: list of (job_id, deadline, profit)
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort by profit

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs:
        for t in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[t] is None:
                slots[t] = job_id
                total_profit += profit
                break

    return slots, total_profit

# Example usage
jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
schedule, profit = job_scheduling(jobs)
print("Schedule:", schedule)
print("Total Profit:", profit)