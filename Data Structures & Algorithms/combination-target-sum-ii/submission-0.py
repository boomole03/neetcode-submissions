class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        combo = []
        candidates.sort()

        
        def dfs(idx, total):
            if total == target:
                res.add(tuple(combo.copy()))
                return

            if total > target or idx > len(candidates) - 1: 
                return 
            
            c = candidates[idx]
            combo.append(c)
            dfs(idx + 1, total + c)

            combo.pop()
            dfs(idx + 1, total)


        dfs(0, 0)
        return [ list(i) for i in res]