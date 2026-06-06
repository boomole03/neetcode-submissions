class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)

        for course, pre in prerequisites:
            pre_map[course].append(pre)

        taken = set()
        trying = set()

        def try_take(course):
            if course in taken: 
                return True

            if course in trying:
                return False

            trying.add(course)
            for pre in pre_map[course]:
                if not try_take(pre):
                    return False
            taken.add(course)
            trying.remove(course)
            return True
        for i in range(numCourses):
            if not try_take(i):
                return False

        return True