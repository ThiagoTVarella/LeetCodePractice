"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}      

        def dfs(root):        

            if not root:
                return None

            if root in visited:
                return visited[root]

            new_node = Node(root.val, [])
            visited[root] = new_node
            neighbors = root.neighbors

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_neighbor = dfs(neighbor)
                    new_node.neighbors.append(new_neighbor)
                else:
                    new_node.neighbors.append(visited[neighbor])

            return new_node

        return dfs(node)
