"""docstring"""
def cutting_stick(length_stick, positions, memo={}):
    """docstring"""
    if len(positions) == 0:
        return 0
    key = (length_stick, tuple(positions))
    if key in memo:
        return memo[key]
    min_cost = float("inf")
    for index in range(len(positions)):
        new_cut = [x - positions[index] for x in positions[index+1:]]
        cost = (
            length_stick +
            cutting_stick(positions[index], positions[:index]) +
            cutting_stick(length_stick - positions[index], new_cut)
            )
        if cost < min_cost:
            min_cost = cost
    memo[key] = min_cost
    return memo[key]

print(cutting_stick(int(input()), [int(val) for val in input().split()]))
