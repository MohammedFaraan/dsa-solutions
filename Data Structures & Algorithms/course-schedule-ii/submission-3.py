class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for nxt, pre in prerequisites:
            adj_list[nxt].append(pre)

        state = [0] * numCourses
        res = []

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1
    
            for nxt_course in adj_list[course]:
                if not dfs(nxt_course):
                    return False
            
            state[course] = 2
            res.append(course)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res