"""Lab 1C: Maximum Earning Jobs"""

def find_max_earning_jobs(num_jobs, jobs):
    """Find the maximum earning jobs"""
    jobs.sort(key=lambda x: int(x[1]))
    opt = [0] * num_jobs
    opt[0] = int(jobs[0][2])
    for index1 in range(1, num_jobs):
        last_job = -1
        for index2 in range(index1-1, -1, -1):
            if int(jobs[index2][1]) <= int(jobs[index1][0]):
                last_job = index2
                break
        if last_job != -1:
            opt[index1] = max(opt[index1-1], opt[last_job] + int(jobs[index1][2]))
        else:
            opt[index1] = max(opt[index1-1], int(jobs[index1][2]))
    return opt[num_jobs-1]

num_jobs = int(input())
jobs = []
for _ in range(num_jobs):
    jobs.append(input().split())
print(find_max_earning_jobs(num_jobs, jobs))
