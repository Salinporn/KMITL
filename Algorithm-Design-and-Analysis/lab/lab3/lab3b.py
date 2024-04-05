"""Lab 3B: Strongly Connected Components"""

def tarjan(graph, nodes_num):
    """Tarjan's Algorithm"""
    global index_counter, index, low_link, on_stack, stack, result
    index_counter = [0]
    index = {}
    low_link = {}
    on_stack = {}
    stack = []
    result = []

    for node in range(1, nodes_num + 1):
        if node not in index:
            strong_connect(node)

    return result

def strong_connect(node):
    """Strongly Connected Components function"""
    index[node] = index_counter[0]
    low_link[node] = index_counter[0]
    index_counter[0] += 1
    stack.append(node)
    on_stack[node] = True

    for neighbor in graph[node]:
        if neighbor not in index:
            strong_connect(neighbor)
            low_link[node] = min(low_link[node], low_link[neighbor])
        elif neighbor in on_stack:
            low_link[node] = min(low_link[node], index[neighbor])

    if low_link[node] == index[node]:
        component = []
        while True:
            neighbor = stack.pop()
            del on_stack[neighbor]
            component.append(neighbor)
            if neighbor == node:
                break
        result.append(component)

nodes_num = int(input())

while nodes_num != 0:
    graph = [[] for _ in range(nodes_num + 1)]
    while True:
        u, v = map(int, input().split())
        if u == 0 and v == 0:
            break
        graph[u].append(v)

    scc_list = tarjan(graph, nodes_num)
    scc_list.sort(key=lambda x: min(x))

    for scc in scc_list:
        print(" ".join(map(str, sorted(scc))))
    break
