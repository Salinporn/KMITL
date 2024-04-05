def find_shortest_path(graph, start, end):
    visited = set()
    queue = [(start, [])]

    while queue:
        current, path = queue.pop(0)

        if current == end:
            return path + [current]

        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                queue.append((neighbor, path + [current]))

    return None

node_num = int(input())
s, t = map(int, input().split())
graph = {i: [] for i in range(1, node_num + 1)}

while True:
    u, v = map(int, input().split())
    if u == 0 and v == 0:
        break
    graph[u].append(v)
result = find_shortest_path(graph, s, t)
if result:
    print(" ".join(map(str, result)))
else:
    print("No path")