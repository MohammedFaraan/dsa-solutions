class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))

        minHeap = [(0, k)]
        visit = set()
        res = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = max(res, time)
            for nei, neiTime in adj_list[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (time + neiTime, nei))
                

        return res if len(visit) == n else -1