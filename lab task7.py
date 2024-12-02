class Node:
  
  def __init__(self, parent=None, position=None):
  
    self.parent = parent
    self.position = position
    self.g = 0 # Cost from start to this node
    self.h = 0 # Heuristic - estimated cost from this node to goal
    self.f = 0 # Total cost (f = g + h)
  
  def __eq__(self, other):
    return self.position == other.position

def a_star_algorithm(start, end, grid):
  """
  Performs the A* algorithm to find the shortest path on a given grid.
  
  :param start: Start point (x, y) coordinates
  :param end: End point (x, y) coordinates
  :param grid: Input 2D array containing obstacles
  :return: list of coordinates (x, y) representing the shortest path
  """

  open_list = []
  closed_list = []

  # Create start and end nodes
  start_node = Node(None, start)
  end_node = Node(None, end)

  # Add the start node to the open list
  open_list.append(start_node)

  while open_list:
    # Get the node with the lowest f value
    current_node = min(open_list, key=lambda node: node.f)

    # Pop current node from open list and add it to closed list
    open_list.remove(current_node)
    closed_list.append(current_node)

    # If we reached the goal, reconstruct the path
    if current_node == end_node:
      path = []
      current = current_node
      while current:
        path.append(current.position)
        current = current.parent
      return path[::-1] # Return reversed path (from start to goal)

    # Generate children (neighbors)
    neighbors = [
      (0, -1), # Up
      (0, 1), # Down
      (-1, 0), # Left
      (1, 0)  # Right
    ]

    for next in neighbors:
      new_position = (current_node.position[0] + next[0], current_node.position[1] + next[1])
      if new_position in closed_list:
        continue
      if grid[new_position[1]][new_position[0]] == 1:
        continue
      new_node = Node(current_node, new_position)
      open_list.append(new_node)

