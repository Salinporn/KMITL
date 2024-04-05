"""Lab 3A: Articulation Points"""

def dfs(u, visited, parent, low, disc, ap, time, graph):
    """Depth First Search function"""
    children = 0
    visited[u] = True
    disc[u] = low[u] = time
    time += 1
    for v in graph[u]:
        if not visited[v]:
            children += 1
            parent[v] = u
            dfs(v, visited, parent, low, disc, ap, time, graph)
            low[u] = min(low[u], low[v])
            if parent[u] == -1 and children > 1:
                ap[u] = True
            if parent[u] != -1 and low[v] >= disc[u]:
                ap[u] = True
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

def find_cities(num, graph):
    """Find the articulation points in the graph"""
    visited = {node: False for node in graph}
    disc = {node: float("inf") for node in graph}
    low = {node: float("inf") for node in graph}
    parent = {node: -1 for node in graph}
    ap = {node: False for node in graph}
    time = 0

    for node in graph:
        if not visited[node]:
            dfs(node, visited, parent, low, disc, ap, time, graph)

    cities = [node for node in ap if ap[node]]
    return cities

def main():
    num = int(input())
    graph = {}
    node = input().split()

    while int(node[0]) != 0 and int(node[1]) != 0:
        node0, node1 = int(node[0]), int(node[1])
        graph.setdefault(node0, []).append(node1)
        graph.setdefault(node1, []).append(node0)
        node = input().split()

    result = find_cities(num, graph)

    print(*result)

if __name__ == "__main__":
    main()
