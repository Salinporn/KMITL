def is_bipartite(graph, node):
    color = [-1] * (node + 1)
    color[1] = 0
    queue = [1]

    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                return False, None, None

    group1 = [i for i in range(1, node + 1) if color[i] == 0]
    group2 = [i for i in range(1, node + 1) if color[i] == 1]
    return True, group1, group2


node = int(input())
graph = {i: [] for i in range(1, node + 1)}

while True:
    u, v = map(int, input().split())
    if u == 0 and v == 0:
        break
    graph[u].append(v)
    graph[v].append(u)

possible, group1, group2 = is_bipartite(graph, node)

if possible:
    print(" ".join(map(str, group1)))
    print(" ".join(map(str, group2)))
else:
    print("Not possible")
