class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        candidates.sort()

        
        def dfs(idx, total):
            if total == target:
                res.append(combo.copy())
                return

            if total > target or idx > len(candidates) - 1: 
                return 
            
            c = candidates[idx]
            combo.append(c)
            dfs(idx + 1, total + c)

            combo.pop()
            next_idx = idx + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
                next_idx += 1
            dfs(next_idx, total)


        dfs(0, 0)
        return res