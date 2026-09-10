class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
            indegree[pre] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for neiCourse in adj_list[course]:
                indegree[neiCourse] -= 1
                if indegree[neiCourse] == 0:
                    q.append(neiCourse)
        
        return res[::-1] if len(res) == numCourses else []