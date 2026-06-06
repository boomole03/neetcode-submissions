class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        dfs through the undirected graph if not in seen... and then add to the counter
        """

        comp = 0

        adj_map = defaultdict(list)
        for u, v in edges:
            adj_map[v].append(u)
            adj_map[u].append(v)

        seen = set()

        def dfs(node):
            for child in adj_map[node]:
                if child not in seen:
                    seen.add(child)
                    dfs(child)



        for node in range(n):
            if node not in seen:
                seen.add(node)
                dfs(node)
                comp += 1

        return comp