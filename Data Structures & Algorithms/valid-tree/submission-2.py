class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < (n - 1):
            return False

        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
                  
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                
                if nei in visit:
                    return False
                
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        