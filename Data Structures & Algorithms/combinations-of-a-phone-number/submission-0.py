class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []

        res = []
        stack = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(stack))
                return 
            
            for d in letter_map[digits[i]]:
                stack.append(d)
                dfs(i+1)
                stack.pop()

            return
        
        dfs(0)
        return res















