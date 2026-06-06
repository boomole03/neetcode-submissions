class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return ''

        res = []

        def backtrack(cur, left, right):
            if left == right == n:
                res.append(''.join(cur))

            if left < n: 
                cur.append('(')
                backtrack(cur, left +1, right)
                cur.pop()
            
            if right < left:
                cur.append(')')
                backtrack(cur, left, right +1)
                cur.pop()
        backtrack([], 0,0)
        return res