class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, t in times:
            adj_list[u].append((t, v))
        
        q = [(0, k)]
        visit = [False] * (n + 1)
        visit_count = 0
        res = 0

        while q:
            t, node = heapq.heappop(q)

            if visit[node]:
                continue
            
            res = max(res, t)
            visit[node] = True
            visit_count += 1
            if visit_count == n:
                return res
            for nieT, nieN in adj_list[node]:
                if not visit[nieN]:
                    heapq.heappush(q, (t + nieT, nieN))
        
        return res if visit_count == n else -1
        

