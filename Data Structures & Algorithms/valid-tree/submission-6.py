class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj_map = defaultdict(list)

        for v, u in edges:
            adj_map[v].append(u)
            adj_map[u].append(v)

        """
        0: [1, 2, 3]
        1: [0, 4]
        2: [0]
        3: [0]
        4: [1]

        1 ----------- 0 --------- 3
        |             |
        |             |
        4             2

        seen = []
        """
        seen = set()
        def has_cycle(node, parent):
            if node in seen:
                return False

            seen.add(node)
            for child in adj_map[node]:
                if child == parent: 
                    # skip this
                    continue
                
                if not has_cycle(child, node):
                    return False
            return True

        return has_cycle(0, -1) and len(seen) == n