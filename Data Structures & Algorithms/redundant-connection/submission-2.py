class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = [[] for _ in range(n+1)]
        indegree = [0] * (n + 1)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            indegree[node] -= 1

            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        
        return []
        