class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visiting = set()
        visited = []

        def dfs(node, parent):
            if node in visiting:
                return False
            
            visiting.add(node)
            visited.append(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            visiting.remove(node)
            return True
        
        if not dfs(0, -1):
            return False
        
        return True if len(visited) == n else False