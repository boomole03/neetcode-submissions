class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        """
        perform topoligocal sort on the prereqs
        """

        # create a graph
        course_map = defaultdict(list)
        for course, pre in prerequisites: 
            course_map[course].append(pre)
        
        current = set()
        seen = set()

        def dfs(course):
            if course in seen: 
                # we have gone through this and it's been validated
                return True

            if course in current: 
                # we have seen this before so it's a cycle
                return False

            current.add(course)

            for pre in course_map[course]:
                if not dfs(pre):
                    return False

            current.remove(course)
            seen.add(course)
            return True

        keys = course_map.keys()

        for c in list(keys):
            # dfs time
            if not dfs(c):
                return False
        
        return True
        