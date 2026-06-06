class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(list)

        for course, pre in prerequisites:
            pre_map[course].append(pre)

        taken = set()
        try_to_take = set()
        res = []

        def topo_search(course):
            if course in taken: 
                return True

            if course in try_to_take: 
                return False

            try_to_take.add(course)
            for c in pre_map[course]:
                if not topo_search(c):
                    return False

            try_to_take.remove(course)
            taken.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not topo_search(course):
                return []

        return res