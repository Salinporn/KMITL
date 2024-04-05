def subsetsum(subs, goal):
    summ = goal
    if summ == 0:
        return True
    if len(subs) == 0:
        return False
    if int(subs[-1]) > summ:
        return subsetsum(subs[:-1], summ)
    return subsetsum(subs[:-1], summ-int(subs[-1])) or subsetsum(subs[:-1], summ)
print(subsetsum(list(map(int, input().split())), int(input())))