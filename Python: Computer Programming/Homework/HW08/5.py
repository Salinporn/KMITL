def shortlong(short, long):
    tf = False
    i = 0
    while len(short) + i <= len(long):
        sub = long[i:len(short) + i]
        if short != sub:
            tf = False
        else:
            tf = True
            break
        i += 1
    return tf


def LCS(s1, s2):
    lst = []
    for i in range(len(s1)):
        for j in range(len(s1)+1):
            sub = s1[i:j]
            if len(sub) > 0:
                if shortlong(sub, s2):
                    lst += [sub]
    common = ""
    for s in lst:
        if len(s) > len(common):
            common = s
    return print(common)


LCS("ingenious", "intelligent")
LCS("philosophically", "zoophilous")
LCS("scada", "kmitl")
LCS("interactive", "inaction")
LCS("multiverse", "metaverse")
