"""Lab3C"""
book_orders = []
books = input()
while books != "#":
    book_orders.append(books)
    books = input()

def topological_helper(node, graph, visited, stack):
    """Topological Sort Helper"""
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            topological_helper(neighbor, graph, visited, stack)
    stack.append(node)

def topological(graph):
    """Topological Sort Algorithm"""
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            topological_helper(node, graph, visited, stack)
    return stack[::-1]

def order_book_alphabet(book_orders):
    """Order Book By Alphabet Function"""
    graph = {}
    for order in book_orders:
        for char in order:
            if char not in graph:
                graph[char] = []
    for i in range(len(book_orders) - 1):
        order1 = book_orders[i]
        order2 = book_orders[i + 1]
        min_length = min(len(order1), len(order2))
        for j in range(min_length):
            if order1[j] != order2[j]:
                graph[order1[j]].append(order2[j])
                break
    sorted_chars = topological(graph)
    return ''.join(sorted_chars)

print(order_book_alphabet(book_orders))
