class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        adj_list = collections.defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))
            
        # Min-heap: stores (cumulative_time, node)
        minHeap = [(0, k)]
        
        # Using a fixed-size array/list is faster than a set in Python for dense lookups
        visited = [False] * (n + 1)
        visited_count = 0
        res = 0
        
        while minHeap:
            time, node = heapq.heappop(minHeap)
            
            if visited[node]:
                continue
                
            visited[node] = True
            visited_count += 1
            res = max(res, time)
            
            # Optimization: Stop early if we have visited all nodes
            if visited_count == n:
                return res
            
            for nei, neiTime in adj_list[node]:
                if not visited[nei]:
                    heapq.heappush(minHeap, (time + neiTime, nei))
                    
        return res if visited_count == n else -1