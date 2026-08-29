class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visit = [False] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            for nei in graph[node]:    
                if not visit[nei]:       
                    visit[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
                
        return res