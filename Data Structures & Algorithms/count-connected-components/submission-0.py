class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()
        def dfs(node, parent):
            visit.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                
                if nei not in visit:
                    dfs(nei, node)

        cnt = 0
        for node in range(n):
            if node not in visit:
                cnt += 1
                dfs(node, -1)
                

        return cnt