class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxHeap = [[cnt, char] for char, cnt in count.items()]

        heapq.heapify_max(maxHeap)

        q = deque()
        time = 0
        res = ""

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][2]
            else:
                count, char = heapq.heappop_max(maxHeap)
                res += char

                count -= 1
                if count:
                    q.append([count, char, time + 1])
            
            if q and time == q[0][2]:
                count, char, time = q.popleft()
                heapq.heappush_max(maxHeap, [count, char])
        
        for i in range(1, len(res)):
            if res[i-1] == res[i]:
                return ""

        return res
        
