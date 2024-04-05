"""Lab 1B: Maximum Number of Jobs"""
def max_jobs(num_jobs, schedules):
    """Maximum Number of Jobs function"""
    for index in range(int(num_jobs)):
        schedules.append(list(map(int, input().split(" "))))
    schedules.sort(key=lambda x: x[1])
    jobs = [schedules[0]]
    for index in range(1, num_jobs):
        if schedules[index][0] >= jobs[-1][1]:
            jobs.append(schedules[index])
    return len(jobs)

print(max_jobs(int(input()), []))
