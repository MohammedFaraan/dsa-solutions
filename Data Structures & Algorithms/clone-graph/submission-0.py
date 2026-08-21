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

        graph_map = defaultdict(Node)
        visited = set()

        def bfs(node):
            q = deque([node])
            visited.add(node)

            while q:
                old_node = q.popleft()
                graph_map[old_node].val = old_node.val

                for neighbor in old_node.neighbors:
                    graph_map[neighbor].val = neighbor.val

                    graph_map[old_node].neighbors.append(
                        graph_map[neighbor]
                    )
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        
        bfs(node)
        return graph_map[node]