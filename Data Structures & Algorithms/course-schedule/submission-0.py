class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [0, 1] take 1 before 0

        #create the map
        class_map = defaultdict(list)
        for course, pre in prerequisites:
            class_map[course].append(pre)

        current = set()
        seen = set()

        def dfs(course):
            if course in seen:
                return True
            if course in current: 
                return False

            current.add(course)
            for c in class_map[course]:
                if not dfs(c):
                    return False
            current.remove(course)
            seen.add(course)
            return True

        for c in range(numCourses): 
            if not dfs(c):
                return False
        return True
        