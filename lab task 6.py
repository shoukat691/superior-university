#question no 1
def bfs(graph, start):
    visited = set()
    traversal_order = []
    level = [start]

    while level:
        next_level = []
        for node in level:
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                next_level.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
        level = next_level

    return traversal_order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
traversal_order = bfs(graph, start_node)
print(traversal_order)  # Output: ['A', 'B', 'C', 'D', 'E', 'F']

#question no 2
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def bfs(node):
    visited = set()
    traversal_order = []
    queue = deque([node])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node.value)
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

# Example usage:
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')

node1.neighbors = [node2, node3]
node2.neighbors = [node1, node4, node5]
node3.neighbors = [node1, node6]
node4.neighbors = [node2]
node5.neighbors = [node2, node6]
node6.neighbors = [node3, node5]

start_node = node1
traversal_order = bfs(start_node)
print(traversal_order)  # Output: ['A', 'B', 'C', 'D', 'E', 'F']