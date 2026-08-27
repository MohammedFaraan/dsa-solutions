class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
     
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        print(graph)
        visit = set()

        def has_cycle(node, parent):
            visit.add(node)
            
            for nei in graph[node]:
                if nei == parent:
                    continue
                
                if nei in visit:
                    return True
                
                if has_cycle(nei, node):
                    return True

            return False

        if has_cycle(0, -1):
            return False

        return True if len(visit) == n else False