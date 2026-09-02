class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        for src, dest in tickets:
            heapq.heappush(adj_list[src], dest)
        
        res = []
        def dfs(src):
            print(src)

            while adj_list[src]:
                dst = heapq.heappop(adj_list[src])
                dfs(dst)
            
            res.append(src)
        
        dfs("JFK")

        return res[::-1]