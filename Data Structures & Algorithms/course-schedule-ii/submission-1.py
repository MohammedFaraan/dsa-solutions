class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for n in graph[course]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
                
        return res if len(res) == numCourses else []