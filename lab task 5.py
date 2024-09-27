class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.neighbors = []

def dfs(node):
    stack = [node]
    while stack:
        current_node = stack.pop()
        if not current_node.visited:
            current_node.visited = True
            print(current_node.value)
            for neighbor in current_node.neighbors:
                if not neighbor.visited:
                    stack.append(neighbor)

# Example usage:
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.neighbors = [node2, node3]
node2.neighbors = [node4, node5]

dfs(node1)  # Output: 1, 2, 4, 5, 3

#question no 2
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.value)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value)

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal:")
inorder_traversal(root)  # Output: 4, 2, 5, 1, 3

print("Preorder Traversal:")
preorder_traversal(root)  # Output: 1, 2, 4, 5, 3

print("Postorder Traversal:")
postorder_traversal(root)  # Output: 4, 5, 2, 3, 1