"""Lab 2A: Reachable Nodes"""

node_num = int(input())
start_node = int(input())
graph = {}
node = input()

while node != "0  0":
    node = node.split()
    if int(node[0]) not in graph:
        graph[int(node[0])] = []
    graph[int(node[0])].append(int(node[1]))
    node = input()

def find_reachable_node(start_node):
    """Find the reachable nodes from the start node"""
    visited = []
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.insert(0, neighbor)
    return visited

result = sorted(find_reachable_node(start_node))
for index in range(len(result)):
    print(result[index], end=" ")
