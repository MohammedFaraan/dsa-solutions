class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
            indegree[pre] += 1
        
        q = deque([crs for crs in range(numCourses) if indegree[crs] == 0])
        res = []

        while q:
            crs = q.popleft()
            res.append(crs)

            for pre in adj_list[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
            
        return True if len(res) == numCourses else False
