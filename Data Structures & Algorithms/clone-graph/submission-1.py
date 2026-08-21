"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        graph_map = {node: Node(node.val)}

        q = deque([node])

        while q:
            old_node = q.popleft()

            for neighbor in old_node.neighbors:
                if neighbor not in graph_map:
                    graph_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                graph_map[old_node].neighbors.append(
                    graph_map[neighbor]
                )

        return graph_map[node]