class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list) # adjacency list
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        res = []
        visit, cycle =  set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res