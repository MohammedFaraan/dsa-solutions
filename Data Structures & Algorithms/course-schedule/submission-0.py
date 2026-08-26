class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        outgoing = defaultdict(list)

        for a, b in prerequisites:
            indegree[a] += 1
            outgoing[b].append(a)

        q = deque()
        visit = 0
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        while q:
            course = q.popleft()
            visit += 1
            for n in outgoing[course]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
                
        return visit == numCourses