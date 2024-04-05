"""Lab3E"""
cities_num = int(input())
cities = []
graph = []
for _ in range(cities_num):
    city_x, city_y = map(float, input().split())
    cities.append((city_x, city_y))
    graph.append([0] * cities_num)

for index1 in range(cities_num):
    for index2 in range(index1 + 1, cities_num):
        x1, y1 = cities[index1]
        x2, y2 = cities[index2]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        graph[index1][index2] = distance
        graph[index2][index1] = distance

def find_cost(graph):
    """Find Total Cost Function"""
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    key = [float('inf')] * len(graph)
    key[0] = 0
    for _ in range(len(graph)):
        min_key = float('inf')
        min_index = -1
        for index in range(len(graph)):
            if not visited[index] and key[index] < min_key:
                min_key = key[index]
                min_index = index
        visited[min_index] = True

        for index in range(len(graph)):
            if not visited[index] and graph[min_index][index] < key[index]:
                key[index] = graph[min_index][index]
                parent[index] = min_index
    return sum(graph[index][parent[index]] for index in range(1, len(graph)))

def find_min_budget(total_cost):
    """Find Minimum Budget Function"""
    min_budget = total_cost * 1.0
    if min_budget == int(min_budget):
        return "{:.1f}".format(min_budget)
    return "{:.2f}".format(min_budget)

print(find_min_budget(find_cost(graph)))
