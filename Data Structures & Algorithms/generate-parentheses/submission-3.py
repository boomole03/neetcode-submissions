class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, par):
            if l == r == n:
                res.append("".join(par))
                return

            if l < n:
                par.append('(')
                dfs(l+1, r, par)
                par.pop()
            
            if r < l:
                par.append(')')
                dfs(l, r+1, par)
                par.pop()


        dfs(0, 0, [])
        return res